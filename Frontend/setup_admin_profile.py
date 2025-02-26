import tkinter as tk
import customtkinter as ctk
from Backend.get_admin_profile import get_admin_profile

def setup_admin_profile(tab, admin_id):
    # Clear previous widgets
    for widget in tab.winfo_children():
        widget.destroy()

    # Fetch admin profile details
    admin_profile = get_admin_profile(admin_id)
    if not admin_profile:
        ctk.CTkLabel(tab, text="Error: Unable to fetch admin profile.", font=ctk.CTkFont(size=16)).pack(pady=20)
        return

    
    # Admin ID
    frame_admin_id = ctk.CTkFrame(tab)
    frame_admin_id.pack(pady=5)
    ctk.CTkLabel(frame_admin_id, text="Admin ID: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_admin_id, text=admin_profile[0], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # Adminname Name
    frame_admin_name = ctk.CTkFrame(tab)
    frame_admin_name.pack(pady=5)
    ctk.CTkLabel(frame_admin_name, text="Admin Name: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_admin_name, text=admin_profile[1], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # First Name
    frame_first_name = ctk.CTkFrame(tab)
    frame_first_name.pack(pady=5)
    ctk.CTkLabel(frame_first_name, text="First Name: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_first_name, text=admin_profile[2], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # Last Name
    frame_last_name = ctk.CTkFrame(tab)
    frame_last_name.pack(pady=5)
    ctk.CTkLabel(frame_last_name, text="Last Name: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_last_name, text=admin_profile[3], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # Email ID
    frame_email_id = ctk.CTkFrame(tab)
    frame_email_id.pack(pady=5)
    ctk.CTkLabel(frame_email_id, text="Email ID: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_email_id, text=admin_profile[4], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # Phone
    frame_phone = ctk.CTkFrame(tab)
    frame_phone.pack(pady=5)
    ctk.CTkLabel(frame_phone, text="Phone: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_phone, text=admin_profile[5], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # DOB
    frame_dob = ctk.CTkFrame(tab)
    frame_dob.pack(pady=5)
    ctk.CTkLabel(frame_dob, text="DOB: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_dob, text=admin_profile[6], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

    # Address
    frame_address = ctk.CTkFrame(tab)
    frame_address.pack(pady=5)
    ctk.CTkLabel(frame_address, text="Address: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_address, text=admin_profile[7], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)

     # Created On
    frame_created_on = ctk.CTkFrame(tab)
    frame_created_on.pack(pady=5)
    ctk.CTkLabel(frame_created_on, text="Created On: ", font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    ctk.CTkLabel(frame_created_on, text=admin_profile[9], font=ctk.CTkFont(size=14)).pack(side="left", padx=10)
    
