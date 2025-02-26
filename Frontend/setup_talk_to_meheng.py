import customtkinter as ctk
from talk_to_meheng import talk_to_meheng

# Define the function to set up the "Talk to Meheng" tab
def setup_talk_to_meheng_tab(tab_talk_to_meheng, user_id, firstname):
    # Create the circular button
    button_talk = ctk.CTkButton(master=tab_talk_to_meheng, text="Talk to Meheng", width=100, height=100, corner_radius=100,font=ctk.CTkFont(family="Helvetica", size=20), fg_color="blue",command=lambda: talk_to_meheng(user_id, firstname, label_status))
    button_talk.pack(pady=20)

    # Create the status label below the button
    label_status = ctk.CTkLabel(tab_talk_to_meheng, text="Ready", font=ctk.CTkFont(family="Helvetica", size=16))
    label_status.pack(pady=10)