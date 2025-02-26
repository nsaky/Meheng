from Backend.establish_backend import establish_backend
from Backend.review_user_account import get_objectionable_chats
import customtkinter as ctk
from tkinter import messagebox

def setup_review_user(tab, admin_id):
    # Clear previous widgets
    for widget in tab.winfo_children():
        widget.destroy()

    # Create input label and entry for User ID
    user_id_label = ctk.CTkLabel(tab, text="Enter User ID to Review:")
    user_id_label.pack(pady=10)

    user_id_entry = ctk.CTkEntry(tab, width=200)
    user_id_entry.pack(pady=10)

    # Status label for displaying messages
    status_label = ctk.CTkLabel(tab, text="", font=ctk.CTkFont(size=12, weight="bold"))
    status_label.pack(pady=5)

    # Create Review User button
    review_button = ctk.CTkButton(tab, text="Review User", command=lambda: review_user_account(user_id_entry.get(), admin_id, tab, status_label))
    review_button.pack(pady=10)

    return status_label  # Ensure this line is added to return status_label

def review_user_account(user_id, admin_id, tab, status_label):
    conn, cursor = establish_backend()

    if not conn or not cursor:
        print("Failed to establish backend connection.")
        return False

    try:
        cursor.execute("SELECT admin_id, actions FROM User WHERE user_id = %s", (user_id,))
        user_info = cursor.fetchone()

        if user_info:
            user_admin_id, actions = user_info

            if user_admin_id != admin_id:
                status_label.configure(text="You are not authorized to review this user account.", text_color="red")
                return False
            
            if actions == 1:
                # Clear previous content in the tab as actions are detected
                for widget in tab.winfo_children():
                    widget.destroy()

                # If there are pending actions, retrieve objectionable chats
                objectionable_chats = get_objectionable_chats(user_id)

                # Display the objectionable chats in a table format
                if objectionable_chats:
                    display_objectionable_chats(tab, objectionable_chats)
                else:
                    no_chats_label = ctk.CTkLabel(tab, text="No objectionable chats found for this user.", font=ctk.CTkFont(size=12))
                    no_chats_label.pack(pady=10)

                # Create buttons for further actions
                action_frame = ctk.CTkFrame(tab)
                action_frame.pack(pady=10)

                # Reselect User button
                reselect_button = ctk.CTkButton(action_frame, text="Reselect User", command=lambda: setup_review_user(tab, admin_id))
                reselect_button.pack(side="left", padx=10)

                # Unban User button
                unban_button = ctk.CTkButton(action_frame, text="Unban User", command=lambda: confirm_unban(user_id, admin_id, tab))
                unban_button.pack(side="left", padx=10)

            else:
                status_label.configure(text="This user has no pending actions.", text_color="red")

        else:
            status_label.configure(text="User not found.", text_color="red")

    except Exception as e:
        print("An error occurred while reviewing the account:", e)

    finally:
        conn.close()

def create_chat_table(tab):
    table_header = ctk.CTkLabel(tab, text="Objectionable Chats", font=ctk.CTkFont(size=14))
    table_header.pack(pady=10)

    headers = ["Query", "Response", "Logged At"]
    header_frame = ctk.CTkFrame(tab)
    header_frame.pack(pady=5)

    for header in headers:
        ctk.CTkLabel(header_frame, text=header, font=ctk.CTkFont(weight="bold")).pack(side="left", padx=5)

def display_objectionable_chats(tab, objectionable_chats):
    for chat in objectionable_chats:
        query, response, log_time = chat
        chat_frame = ctk.CTkFrame(tab)
        chat_frame.pack(pady=5)
        ctk.CTkLabel(chat_frame, text=query).pack(side="left", padx=5)
        ctk.CTkLabel(chat_frame, text=response).pack(side="left", padx=5)
        ctk.CTkLabel(chat_frame, text=log_time).pack(side="left", padx=5)

def confirm_unban(user_id, admin_id, tab):
    if messagebox.askyesno("Confirm Unban", "Do you want to unban this user? Note that if you confirm, they will be able to log in to their account and all their objectionable chats will be flagged as unobjectionable."):
        unban_user(user_id, admin_id, tab)

def unban_user(user_id, admin_id, tab):
    conn, cursor = establish_backend()

    if not conn or not cursor:
        print("Failed to establish backend connection.")
        return False

    try:
        cursor.execute("UPDATE User SET actions = 0 WHERE user_id = %s", (user_id,))
        cursor.execute("UPDATE ConversationLogs SET is_objectionable = 0 WHERE user_id = %s", (user_id,))
        conn.commit()

        messagebox.showinfo("Success", f"User {user_id} has been unbanned and their objectionable chats have been cleared.")
        
        # Clear the tab for fresh review
        setup_review_user(tab, admin_id)

    except Exception as e:
        print("An error occurred while unbanning the user:", e)

    finally:
        conn.close()
