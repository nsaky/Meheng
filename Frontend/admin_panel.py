import customtkinter as ctk
from Backend.establish_backend import establish_backend

#Importing Frontend functions
from Frontend.logout import logout
from Frontend.setup_admin_chat_history import setup_admin_chat_history
from Frontend.setup_admin_talk_to_meheng import setup_admin_talk_to_meheng_tab
from Frontend.setup_admin_profile import setup_admin_profile
from Frontend.setup_manage_users import setup_manage_users

def show_admin_panel(root, admin_id):
    for widget in root.winfo_children():
        widget.destroy()  # Clear the window

    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    conn, cursor = establish_backend()
    if not conn or not cursor:
        print("Failed to establish backend connection.")
        return

    try:
        query="SELECT first_name FROM Admin WHERE admin_id = '{}'".format(admin_id)
        cursor.execute(query)
        first_name = cursor.fetchone()

        if first_name:
            first_name = first_name[0]
        else:
            print("Admin not found.")
            return

    except Exception as e:
        print("An error occurred while fetching admin data:", e)
        return

    finally:
        conn.close()

    # Create the main frame for the Admin panel
    frame_main = ctk.CTkFrame(root)
    frame_main.pack(pady=0, padx=10, fill="both", expand=True)

    # Top Section with padding and border
    frame_top = ctk.CTkFrame(frame_main)
    frame_top.pack(fill='x', padx=0, pady=0)

    label_greeting = ctk.CTkLabel(frame_top, text=f"Hi, {first_name}", font=ctk.CTkFont(family="Helvetica", size=30, weight="bold"))
    label_greeting.pack(side="left", padx=20, pady=20)

    label_admin_id = ctk.CTkLabel(frame_top, text=f"Admin ID: {admin_id}", font=ctk.CTkFont(family="Helvetica", size=14))
    label_admin_id.pack(side="left", padx=0, pady=(10, 0))

    button_logout = ctk.CTkButton(frame_top, text="Logout", command=lambda: logout(root), border_width=2, fg_color="red", corner_radius=5)
    button_logout.pack(side="right", padx=20, pady=20)

    # Tab View
    tabview = ctk.CTkTabview(master=frame_main)
    tabview.pack(pady=10, fill="both", expand=True)

    # Create tabs
    tab_talk_to_meheng = tabview.add("Talk to Meheng")
    tab_chat_history = tabview.add("Chat History")
    tab_manage_users = tabview.add("Manage Users")
    tab_profile = tabview.add("Profile")

    # Setup the tabs
    setup_admin_talk_to_meheng_tab(tab_talk_to_meheng, admin_id, first_name)
    setup_admin_chat_history(tab_chat_history, admin_id)
    setup_manage_users(tab_manage_users,admin_id)
    setup_admin_profile(tab_profile, admin_id)

    # Set the default tab
    tabview.set("Talk to Meheng")
