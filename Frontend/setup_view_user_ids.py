import customtkinter as ctk
from Backend.get_all_users_under_admin import get_all_users_under_admin

def setup_view_user_ids(tab, admin_id):
    # Clear the tab
    for widget in tab.winfo_children():
        widget.destroy()

    # Fetch all users under the admin
    users = get_all_users_under_admin(admin_id)

    # Create a frame for the table
    frame_table = ctk.CTkFrame(tab)
    frame_table.pack(pady=20, padx=20, fill="both", expand=True)

    # Create headers
    headers = ["S.No", "User ID", "Username", "Name", "Email", "Actions"]
    for col, header in enumerate(headers):
        label = ctk.CTkLabel(frame_table, text=header, font=ctk.CTkFont(family="Helvetica", size=14, weight="bold"))
        label.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")  # Center align header labels
        frame_table.grid_columnconfigure(col, weight=1)  # Make columns stretch equally
        # Set background color for the header

    # Populate the table with user data
    for row, user in enumerate(users, start=1):  # Start enumeration at 1 for S.No
        user_id, username, name, email, actions = user
        labels = [
            ctk.CTkLabel(frame_table, text=str(row), anchor="center"),  # S.No
            ctk.CTkLabel(frame_table, text=user_id, anchor="center"),
            ctk.CTkLabel(frame_table, text=username, anchor="center"),
            ctk.CTkLabel(frame_table, text=name, anchor="center"),
            ctk.CTkLabel(frame_table, text=email, anchor="center"),
            ctk.CTkLabel(frame_table, text=actions, anchor="center"),
        ]
        
        for col, label in enumerate(labels):
            label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")  # Center align all labels
            frame_table.grid_columnconfigure(col, weight=1)  # Make columns stretch equally
