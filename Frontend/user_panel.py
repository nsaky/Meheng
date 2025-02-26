import customtkinter as ctk
from Backend.establish_backend import establish_backend
from Frontend.logout import logout
from Frontend.setup_talk_to_meheng import setup_talk_to_meheng_tab
from Frontend.setup_chat_history import setup_chat_history
from Frontend.setup_user_profile import setup_user_profile

def show_user_panel(root, user_id):
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Establish backend connection to retrieve user details
    conn, cursor = establish_backend()
    if not conn or not cursor:
        print("Failed to establish backend connection.")
        return

    try:
        # Fetch user first name using the user_id
        query="SELECT first_name FROM User WHERE user_id = '{}'".format(user_id)
        cursor.execute(query)
        first_name = cursor.fetchone()

        if first_name:
            first_name = first_name[0]
        else:
            print("User not found.")
            return

    except Exception as e:
        print("An error occurred while fetching user data:", e)
        return

    finally:
        conn.close()

    # Create the main frame for the user panel
    frame_main = ctk.CTkFrame(root)
    frame_main.pack(pady=0, padx=10, fill="both", expand=True)

    # Top Section with padding and border
    frame_top = ctk.CTkFrame(frame_main)
    frame_top.pack(fill='x', padx=0, pady=0)

    label_greeting = ctk.CTkLabel(frame_top, text=f"Hi, {first_name}", font=ctk.CTkFont(family="Helvetica", size=30, weight="bold"))
    label_greeting.pack(side="left", padx=20, pady=20)

    label_user_id = ctk.CTkLabel(frame_top, text=f"User ID: {user_id}", font=ctk.CTkFont(family="Helvetica", size=14))
    label_user_id.pack(side="left", padx=0, pady=(10, 0))

    button_logout = ctk.CTkButton(frame_top, text="Logout", command=lambda: logout(root), border_width=2, fg_color="red", corner_radius=5)
    button_logout.pack(side="right", padx=20, pady=20)

    # Tab View
    tabview = ctk.CTkTabview(master=frame_main)
    tabview.pack(pady=10, fill="both", expand=True)

    # Create tabs
    tab_talk_to_meheng = tabview.add("Talk to Meheng")
    tab_chat_history = tabview.add("Chat History")
    tab_profile = tabview.add("Profile")

    # Setup the tabs
    setup_talk_to_meheng_tab(tab_talk_to_meheng, user_id, first_name)
    setup_chat_history(tab_chat_history, user_id)
    setup_user_profile(tab_profile, user_id)

    # Set the default tab
    tabview.set("Talk to Meheng")
