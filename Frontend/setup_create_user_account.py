import customtkinter as ctk
from tkinter import messagebox
from Backend.create_user_account import create_user_account
from Backend.create_user_account import get_all_username_email

def setup_create_user_account(tab, admin_id):
    # Clear previous widgets
    for widget in tab.winfo_children():
        widget.destroy()

    # Create a frame to hold the form and center it
    form_frame = ctk.CTkFrame(tab)
    form_frame.pack(expand=True)

    # Create form labels and entries inside the frame
    labels = ["Username*", "First Name*", "Last Name", "Email*", "Phone", "DOB (YYYY-MM-DD)", "Address", "Password*", "Confirm Password*"]
    entries = {}

    for i, label in enumerate(labels):
        ctk.CTkLabel(form_frame, text=label, font=ctk.CTkFont(size=12)).grid(row=i, column=0, padx=20, pady=5, sticky="w")
        entry = ctk.CTkEntry(form_frame)
        entry.grid(row=i, column=1, padx=20, pady=5, sticky="w")
        entries[label] = entry  # Store entry fields in the dictionary for access

    # Add a label for status messages
    status_label = ctk.CTkLabel(form_frame, text="", font=ctk.CTkFont(size=12), text_color="red")
    status_label.grid(row=len(labels), column=0, columnspan=2, pady=10)

    # Create account button
    create_button = ctk.CTkButton(form_frame, text="Create Account", command=lambda: validate_and_create_user(admin_id, entries, status_label))
    create_button.grid(row=len(labels) + 1, column=0, columnspan=2, pady=20)

def validate_and_create_user(admin_id, entries, status_label):
    # Retrieve form values
    username = entries["Username*"].get().strip()
    first_name = entries["First Name*"].get().strip()
    last_name = entries["Last Name"].get().strip() or None  # Set to None if not provided
    email = entries["Email*"].get().strip()
    phone = entries["Phone"].get().strip() or None  # Set to None if not provided
    dob = entries["DOB (YYYY-MM-DD)"].get().strip() or None  # Set to None if not provided
    address = entries["Address"].get().strip() or None  # Set to None if not provided
    password = entries["Password*"].get().strip()
    confirm_password = entries["Confirm Password*"].get().strip()

    # Validation checks
    if not username or not first_name or not email or not password or not confirm_password:
        status_label.configure(text="*Fields are mandatory.")
        return

    if password != confirm_password:
        status_label.configure(text="Passwords do not match.")
        return

    # Get all existing usernames and emails for validation
    existing_usernames, existing_emails = get_all_username_email()

    if username in existing_usernames:
        status_label.configure(text="Username already exists. Please choose a different one.")
        return

    if email in existing_emails:
        status_label.configure(text="Email already exists. Please choose a different one.")
        return

    # Phone number and DOB validation
    if phone and not phone.isdigit():
        status_label.configure(text="Phone number must contain only digits.")
        return

    if dob and not validate_dob_format(dob):
        status_label.configure(text="Invalid date format. Use YYYY-MM-DD.")
        return

    # All validation passed, attempt to create account
    user_id, success, error = create_user_account(admin_id, username, first_name, last_name, email, phone, dob, address, password)
    
    if success:
        messagebox.showinfo("Success", f"User account created successfully with user ID: {user_id}")
        clear_form(entries)
    else:
        status_label.configure(text=f"Error: {error}")

# Helper function to clear the form after success
def clear_form(entries):
    for entry in entries.values():
        entry.delete(0, 'end')

# Function to validate date format (YYYY-MM-DD)
def validate_dob_format(dob):
    try:
        year, month, day = map(int, dob.split('-'))
        return 1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 31
    except ValueError:
        return False
