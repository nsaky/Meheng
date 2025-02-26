import customtkinter as ctk
from Backend.user_view_chats import user_view_chats
from Backend.establish_backend import establish_backend
import tkinter.messagebox as messagebox

# Global variable to store the User ID Entry widget and the form container
user_id_entry = None
form_frame = None

def setup_user_chat_history_for_admin(tab, admin_id):
    global user_id_entry, form_frame

    # Clear any existing widgets in the tab
    for widget in tab.winfo_children():
        widget.destroy()

    # Create a frame for the form where user ID is entered
    form_frame = ctk.CTkFrame(tab, width=400)
    form_frame.pack(pady=20, padx=20)

    # Add User ID input
    user_id_label = ctk.CTkLabel(form_frame, text="User ID:", font=ctk.CTkFont(size=14))
    user_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    user_id_entry = ctk.CTkEntry(form_frame, width=200)
    user_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Add "Show User Chats" button
    show_chats_button = ctk.CTkButton(form_frame, text="Show User Chats", command=lambda: verify_user_and_show_chats(tab, status_label, user_id_entry.get(), admin_id))
    show_chats_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Add a placeholder for status messages
    status_label = ctk.CTkLabel(form_frame, text="", font=ctk.CTkFont(size=12),text_color="red")
    status_label.grid(row=2, column=0, columnspan=2, pady=10)


def verify_user_and_show_chats(parent_tab, warning_label, user_id, admin_id):
    conn, cursor = establish_backend()

    if not conn or not cursor:
        warning_label.configure(text="Failed to connect to database.")
        return

    try:
        # Query to fetch the admin_id of the entered user_id
        cursor.execute('''
            SELECT admin_id FROM User WHERE user_id = %s
        ''', (user_id,))
        result = cursor.fetchone()

        if result is None:
            # If no result is returned, the user_id doesn't exist
            warning_label.configure(text="User does not exist.")
        elif result[0] != admin_id:
            # If the admin_id doesn't match the current admin_id
            warning_label.configure(text="This user does not belong to your admin account.")
        else:
            # If the user exists and belongs to the current admin, proceed to load chat history
            warning_label.configure(text="")  # Clear any previous warnings
            # Clear the previous widgets and show chat history tabs
            for widget in parent_tab.winfo_children():
                widget.destroy()
            setup_chat_history(parent_tab, user_id, admin_id)  # Proceed to chat history display

    except Exception as e:
        #warning_label.configure(text=f"An error occurred: {e}")
        print("an error accoured",e)

    finally:
        conn.close()



# Function to set up the Chat History (two subtabs: All Chats and By Date)
def setup_chat_history(tab, user_id, admin_id):
    # Create TabView for "All Chats" and "By Date"
    tabview_chat_history = ctk.CTkTabview(tab)
    tabview_chat_history.pack(pady=20, padx=20, fill="both", expand=True)

    # Add tabs for "All Chats" and "By Date"
    tab_all_chats = tabview_chat_history.add("All Chats")
    tab_by_date = tabview_chat_history.add("By Date")

    # Display "All Chats" initially
    fetch_chats(user_id, tab_all_chats, "all")

    # Setup "By Date" tab with date inputs
    setup_by_date_tab(tab_by_date, user_id)

    # Add a "Reselect User" button to go back to the form
    reselect_user_button = ctk.CTkButton(tab, text="Reselect User", command=lambda: setup_user_chat_history_for_admin(tab, admin_id))
    reselect_user_button.pack(pady=0)

# Function to set up the "By Date" tab with input fields
def setup_by_date_tab(tab, user_id):
    for widget in tab.winfo_children():
        widget.destroy()
    
    # Date input fields and labels
    start_date_label = ctk.CTkLabel(tab, text="Start Date (YYYY-MM-DD):")
    start_date_label.pack(pady=5)
    start_date_entry = ctk.CTkEntry(tab)
    start_date_entry.pack(pady=5)

    end_date_label = ctk.CTkLabel(tab, text="End Date (YYYY-MM-DD):")
    end_date_label.pack(pady=5)
    end_date_entry = ctk.CTkEntry(tab)
    end_date_entry.pack(pady=5)

    # Fetch button to retrieve chats by date
    fetch_button = ctk.CTkButton(tab, text="Fetch Chats", command=lambda: fetch_chats(user_id, tab, "date", start_date_entry.get(), end_date_entry.get()))
    fetch_button.pack(pady=10)

    # Reset date inputs button
    reset_button = ctk.CTkButton(tab, text="Reset Dates", command=lambda: reset_date_inputs(start_date_entry,end_date_entry))
    reset_button.pack(pady=10)

def fetch_chats(user_id, tab, filter_type, start_date=None, end_date=None):
    # Clear previous chat table (if any)
    for widget in tab.winfo_children():
        widget.destroy()

    conn, cursor = establish_backend()
    if not conn or not cursor:
        print("Error")
        return

    try:
        if filter_type == "all":
            chats = user_view_chats(user_id)
        elif filter_type == "date" and start_date and end_date:
            chats = user_view_chats(user_id, start_date, end_date)

        if chats:
            # Create table structure with headers
            table_frame = ctk.CTkFrame(tab)
            table_frame.pack(fill="both", expand=True)

            # Create scrollable frame
            scroll_frame = ctk.CTkScrollableFrame(table_frame, height=320)
            scroll_frame.pack(fill="both", expand=True)

            # Table headers using grid layout for proper alignment
            header_frame = ctk.CTkFrame(scroll_frame)
            header_frame.grid(row=0, column=0, sticky="w")

            headers = ["S.No.", "Date & Time", "Query", "Response"]
            header_widths = [50, 150, 300, 300]  # Set width for each column
            for col, (header, width) in enumerate(zip(headers, header_widths)):
                label_header = ctk.CTkLabel(header_frame, text=header, font=ctk.CTkFont(size=14, weight="bold"))
                label_header.grid(row=0, column=col, padx=10, pady=10)
                header_frame.columnconfigure(col, weight=1)

            # Populate chat history in grid format for proper alignment
            for i, chat in enumerate(chats, start=1):
                query, response, log_time = chat
                log_time = log_time.strftime('%Y-%m-%d %H:%M:%S')

                label_sno = ctk.CTkLabel(scroll_frame, text=str(i))
                label_sno.grid(row=i, column=0, padx=10, pady=10)

                label_log_time = ctk.CTkLabel(scroll_frame, text=log_time)
                label_log_time.grid(row=i, column=1, padx=10, pady=10)

                label_query = ctk.CTkLabel(scroll_frame, text=query, wraplength=280, justify="left")
                label_query.grid(row=i, column=2, padx=10, pady=10, sticky="w")

                label_response = ctk.CTkLabel(scroll_frame, text=response, wraplength=280, justify="left")
                label_response.grid(row=i, column=3, padx=10, pady=10, sticky="w")
            
            if start_date and end_date:
                # Add a button to allow reselecting the dates after fetching chats
                reselect_but = ctk.CTkButton(tab, text="Reselect Dates", command=lambda: setup_by_date_tab(tab, user_id))
                reselect_but.pack(pady=(3,0))
        else:
            print("Error")

    except Exception as e:
        print("Error",e)

    finally:
        conn.close()

# Function to reset the date inputs in the "By Date" tab
def reset_date_inputs(start_date_entry,end_date_entry):
    start_date_entry.delete(0, 'end')
    end_date_entry.delete(0, 'end')
