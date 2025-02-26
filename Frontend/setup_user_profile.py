import tkinter as tk
import customtkinter as ctk
from Backend.get_user_profile import get_user_profile

def setup_user_profile(tab, user_id):
    # Clear previous widgets
    for widget in tab.winfo_children():
        widget.destroy()

    # Fetch user profile details
    user_profile = get_user_profile(user_id)
    if not user_profile:
        ctk.CTkLabel(tab, text="Error: Unable to fetch user profile.", font=ctk.CTkFont(size=16)).pack(pady=20)
        return

    # Manually display user profile details
    # Assuming user_profile is in the form of a tuple: (user_id, first_name, last_name, phone, dob, address, password)
    
    # User ID
    frame_user_id = ctk.CTkFrame(tab)
    frame_user_id.pack(pady=5)
    ctk.CTkLabel(frame_user_id, text="User ID: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_user_id, text=user_profile[0], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # Username Name
    frame_user_name = ctk.CTkFrame(tab)
    frame_user_name.pack(pady=5)
    ctk.CTkLabel(frame_user_name, text="User Name: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_user_name, text=user_profile[1], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # First Name
    frame_first_name = ctk.CTkFrame(tab)
    frame_first_name.pack(pady=5)
    ctk.CTkLabel(frame_first_name, text="First Name: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_first_name, text=user_profile[2], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # Last Name
    frame_last_name = ctk.CTkFrame(tab)
    frame_last_name.pack(pady=5)
    ctk.CTkLabel(frame_last_name, text="Last Name: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_last_name, text=user_profile[3], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # Email ID
    frame_email_id = ctk.CTkFrame(tab)
    frame_email_id.pack(pady=5)
    ctk.CTkLabel(frame_email_id, text="Email ID: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_email_id, text=user_profile[4], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # Phone
    frame_phone = ctk.CTkFrame(tab)
    frame_phone.pack(pady=5)
    ctk.CTkLabel(frame_phone, text="Phone: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_phone, text=user_profile[5], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # DOB
    frame_dob = ctk.CTkFrame(tab)
    frame_dob.pack(pady=5)
    ctk.CTkLabel(frame_dob, text="DOB: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_dob, text=user_profile[6], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # Address
    frame_address = ctk.CTkFrame(tab)
    frame_address.pack(pady=5)
    ctk.CTkLabel(frame_address, text="Address: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_address, text=user_profile[7], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # Admin ID
    frame_password = ctk.CTkFrame(tab)
    frame_password.pack(pady=5)
    ctk.CTkLabel(frame_password, text="Admin ID: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_password, text=user_profile[9], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

     # Created On
    frame_created_on = ctk.CTkFrame(tab)
    frame_created_on.pack(pady=5)
    ctk.CTkLabel(frame_created_on, text="Created On: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_created_on, text=user_profile[11], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    
