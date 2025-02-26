import customtkinter as ctk
from Backend.get_login_activities import get_login_activities

def setup_login_activities(tab, admin_id):
    # Function to create the user ID form and show button
    def create_user_id_form():
        # Clear previous widgets
        for widget in tab.winfo_children():
            widget.destroy()

        # Create a frame for user input and center it
        frame_input = ctk.CTkFrame(tab)
        frame_input.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Center align the input section by placing it within an inner frame
        inner_frame = ctk.CTkFrame(frame_input)
        inner_frame.pack(pady=40)

        # Label and input for User ID
        label_user_id = ctk.CTkLabel(inner_frame, text="User ID:", font=ctk.CTkFont(size=14))
        label_user_id.grid(row=0, column=0, padx=10, pady=10)

        entry_user_id = ctk.CTkEntry(inner_frame, width=200)
        entry_user_id.grid(row=0, column=1, padx=10, pady=10)

        # Status label for feedback
        label_status = ctk.CTkLabel(inner_frame, text="", font=ctk.CTkFont(size=12), text_color="red")
        label_status.grid(row=2, column=0, columnspan=2, pady=10)

        # Function to handle login activity retrieval
        def show_login_activities():
            user_id = entry_user_id.get()

            if not user_id:
                label_status.configure(text="Please enter a User ID.")
                return

            # Fetch login activities from the backend
            status, login_activities = get_login_activities(admin_id, user_id)

            if status:
                label_status.configure(text=status)
                return

            # Clear input form and display the login activities table
            for widget in tab.winfo_children():
                widget.destroy()

            create_login_activity_table(login_activities)

        # Button to show login activities
        button_show = ctk.CTkButton(inner_frame, text="Show Login Activities", command=show_login_activities)
        button_show.grid(row=1, column=0, columnspan=2, padx=50, pady=10)

    # Function to create a scrollable login activities table using CTkScrollableFrame
    def create_login_activity_table(login_activities):
        # Create a scrollable frame for the table
        scrollable_frame = ctk.CTkScrollableFrame(tab, width=600, height=350)  # Adjusted height for better button visibility
        scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Center align the table inside the scrollable frame
        inner_table_frame = ctk.CTkFrame(scrollable_frame)
        inner_table_frame.pack(pady=10, padx=10, anchor="center")

        # Create table headers
        headers = ["Session ID", "Login Time", "IP Address"]
        for col, header in enumerate(headers):
            header_label = ctk.CTkLabel(inner_table_frame, text=header, font=ctk.CTkFont(size=14, weight="bold"))
            header_label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")

        # Display login activities
        for row, activity in enumerate(login_activities, start=1):
            session_id, login_time, ip_address = activity
            labels = [
                ctk.CTkLabel(inner_table_frame, text=str(session_id), anchor="center"),
                ctk.CTkLabel(inner_table_frame, text=str(login_time), anchor="center"),
                ctk.CTkLabel(inner_table_frame, text=ip_address, anchor="center"),
            ]
            for col, label in enumerate(labels):
                label.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")

        # Back button placed outside the scrollable frame
        button_back = ctk.CTkButton(tab, text="Back", command=create_user_id_form)
        button_back.pack(pady=10)  # Positioned outside the scrollable frame, below the table

    # Initial call to create the user ID form
    create_user_id_form()
