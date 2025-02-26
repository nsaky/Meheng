import customtkinter as ctk

from Backend.establish_backend import establish_backend
from Backend.admin_login import admin_login
from Backend.user_login import user_login

ctk.set_appearance_mode("dark")  # Set dark mode
ctk.set_default_color_theme("dark-blue")  # Set default theme color

# Main Application Window
root = ctk.CTk()
root.title("Meheng.ai")
root.geometry("900x600")

# Function to show the main menu with login options
def login_menu():
    for widget in root.winfo_children():
        widget.destroy()  # Clear the window

    frame_body = ctk.CTkFrame(root, fg_color="transparent")  # Transparent frame
    frame_body.pack(pady=10)

    label_title = ctk.CTkLabel(frame_body, text="Meheng.AI", font=ctk.CTkFont(family="Helvetica", size=24, weight="bold"))
    label_title.pack(pady=20)

    label_developed_by = ctk.CTkLabel(frame_body, text="Developed by Md. Yasir Eqbal, Ananya & Shivam Bhardawaj", font=ctk.CTkFont(family="Helvetica", size=14))
    label_developed_by.pack(pady=5)

    button_frame = ctk.CTkFrame(frame_body, fg_color="transparent") 
    button_frame.pack(pady=50)

    button_admin_login = ctk.CTkButton(button_frame, text="Admin Login", command=show_admin_login, border_width=2, fg_color="grey")
    button_admin_login.pack(side="left", padx=20)  # Place side by side

    button_user_login = ctk.CTkButton(button_frame, text="User Login", command=show_user_login, border_width=2, fg_color="grey")
    button_user_login.pack(side="left", padx=20)  # Place side by side

    button_frame.pack(expand=True)  # Center align the button frame

    frame_body.pack(expand=True)


# Function to show the admin login form
def show_admin_login():
    for widget in root.winfo_children():
        widget.destroy()  # Clear the window
    
    frame_body = ctk.CTkFrame(root, fg_color="transparent")
    frame_body.pack(pady=10)


    label_admin = ctk.CTkLabel(frame_body, text="Admin Login", font=ctk.CTkFont(family="Helvetica", size=24, weight="bold"))
    label_admin.pack(pady=20)

    # Admin Name and Password fields with labels beside
    frame_adminname = ctk.CTkFrame(frame_body, fg_color="transparent")
    frame_adminname.pack(pady=10)

    frame_adminpass = ctk.CTkFrame(frame_body, fg_color="transparent")
    frame_adminpass.pack(pady=10)

    label_admin_name = ctk.CTkLabel(frame_adminname, text="Admin Name:")
    label_admin_name.pack(side="left", padx=(0, 5))
    entry_admin_name = ctk.CTkEntry(frame_adminname, placeholder_text="Enter Admin Name")
    entry_admin_name.pack(side="left", padx=5)

    label_admin_password = ctk.CTkLabel(frame_adminpass, text="Password:")
    label_admin_password.pack(side="left", padx=(20, 5))
    entry_admin_password = ctk.CTkEntry(frame_adminpass, placeholder_text="Enter Password", show="*")
    entry_admin_password.pack(side="left", padx=5)

    # Submit and Back buttons on the same line
    button_frame = ctk.CTkFrame(frame_body, fg_color="transparent")
    button_frame.pack(pady=20)

    label_feedback = ctk.CTkLabel(frame_body, text="", font=ctk.CTkFont(size=12))
    label_feedback.pack(pady=10)

    button_submit = ctk.CTkButton(button_frame, text="Submit", command=lambda:admin_login(root, entry_admin_name, entry_admin_password, label_feedback), fg_color="grey", border_width=2)
    button_submit.pack(side="left", padx=10)

    button_back = ctk.CTkButton(button_frame, text="Back", command=login_menu, fg_color="red", border_width=2)
    button_back.pack(side="left", padx=10)

    frame_body.pack(expand=True) 

# Function to show the user login form
def show_user_login():
    for widget in root.winfo_children():
        widget.destroy()  # Clear the window

    frame_body = ctk.CTkFrame(root, fg_color="transparent")  # Transparent frame
    frame_body.pack(pady=10)

    label_user = ctk.CTkLabel(frame_body, text="User Login", font=ctk.CTkFont(family="Helvetica", size=24, weight="bold"))
    label_user.pack(pady=20)

    frame_username = ctk.CTkFrame(frame_body, fg_color="transparent")  # Transparent frame
    frame_username.pack(pady=10)

    frame_userpass = ctk.CTkFrame(frame_body, fg_color="transparent")  # Transparent frame
    frame_userpass.pack(pady=10)

    label_user_name = ctk.CTkLabel(frame_username, text="Username:")
    label_user_name.pack(side="left", padx=(0, 5))
    entry_user_name = ctk.CTkEntry(frame_username, placeholder_text="Enter Username")
    entry_user_name.pack(side="left", padx=5)

    label_user_password = ctk.CTkLabel(frame_userpass, text="Password:")
    label_user_password.pack(side="left", padx=(20, 5))
    entry_user_password = ctk.CTkEntry(frame_userpass, placeholder_text="Enter Password", show="*")
    entry_user_password.pack(side="left", padx=5)

    # Submit and Back buttons on the same line
    button_frame = ctk.CTkFrame(frame_body, fg_color="transparent")  # Transparent frame for buttons
    button_frame.pack(pady=20)

    label_feedback = ctk.CTkLabel(frame_body, text="", font=ctk.CTkFont(size=12))  # Initially empty for feedback
    label_feedback.pack(pady=10)

    button_submit = ctk.CTkButton(button_frame, text="Submit", command=lambda:user_login(root, entry_user_name, entry_user_password, label_feedback), fg_color="grey", border_width=2)
    button_submit.pack(side="left", padx=10)

    button_back = ctk.CTkButton(button_frame, text="Back", command=login_menu, fg_color="red", border_width=2)
    button_back.pack(side="left", padx=10)

    frame_body.pack(expand=True)




# Start with the main menu
login_menu()

# Start the Tkinter event loop
root.mainloop()