import customtkinter as ctk
from Backend.ban_user import ban_user
from tkinter import messagebox

def setup_ban_user(tab, admin_id):
    # Clear previous widgets
    for widget in tab.winfo_children():
        widget.destroy()

    # Create a frame to hold the form and center it
    form_frame = ctk.CTkFrame(tab)
    form_frame.pack(expand=True)

    # Create the label and entry for User ID
    ctk.CTkLabel(form_frame, text="Enter User ID for Ban", font=ctk.CTkFont(size=12)).grid(row=0, column=0, padx=20, pady=10, sticky="w")
    user_id_entry = ctk.CTkEntry(form_frame, width=200)
    user_id_entry.grid(row=0, column=1, padx=20, pady=10)

    # Add a label for status messages
    status_label = ctk.CTkLabel(form_frame, text="", font=ctk.CTkFont(size=12), text_color="red")
    status_label.grid(row=2, column=0, columnspan=2, pady=10)

    # Ban user button
    ban_button = ctk.CTkButton(form_frame, text="Ban User", command=lambda: validate_and_ban_user(admin_id, user_id_entry, status_label))
    ban_button.grid(row=1, column=0, columnspan=2, pady=20)

from tkinter import messagebox  # Import messagebox from tkinter

def validate_and_ban_user(admin_id, user_id_entry, status_label):
    user_id = user_id_entry.get()

    if not user_id:
        status_label.configure(text="User ID cannot be empty.", text_color="red")
        return

    else: 
        # Show a confirmation dialog before banning the user
        confirm_ban = messagebox.askyesno("Confirmation", 
            f"Are you sure you want to ban User ID {user_id}? Note: They won't be able to log into their account if you confirm.")
        
        if confirm_ban:
            ban_success, message = ban_user(admin_id, user_id)
            # If the admin confirms, ban the user and show a success message
            status_label.configure(text="")  # Clear any previous error
            messagebox.showinfo("Success", message)  # Display success message in a message box
            user_id_entry.delete(0, 'end')  # Clear the user ID field
        else:
            # If the admin cancels, update the status label
            status_label.configure(text="Ban operation canceled.", text_color="blue")



