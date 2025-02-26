from Backend.establish_backend import establish_backend
from Backend.track_login_activity import track_login_activity
from Frontend.admin_panel import show_admin_panel

def admin_login(root, entry_admin_name,entry_admin_password, label_feedback):
    admin_name = entry_admin_name.get()
    entered_password = entry_admin_password.get()
    
    conn, cursor = establish_backend()

    if not conn or not cursor:
        print("Failed to establish backend connection.")
        return False

    try:
        query = "SELECT admin_id, password FROM Admin WHERE adminname = '{}'".format(admin_name)
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            admin_id, stored_password = result

            if entered_password == stored_password:
                track_login_activity(admin_id)
                # Clear the window and show admin panel
                show_admin_panel(root, admin_id)
            else:
                label_feedback.configure(text="Incorrect password. Please try again.", text_color="red")
        else:
            label_feedback.configure(text="Admin name does not exist.", text_color="red")

    except Exception as e:
        print("An error occurred while logging in:", e)

    finally:
        conn.close()

