from Backend.establish_backend import establish_backend
from Backend.track_login_activity import track_login_activity
from Frontend.user_panel import show_user_panel

def user_login(root, entry_user_name, entry_user_password, feedback_label):
    username = entry_user_name.get()
    entered_password = entry_user_password.get()
    conn, cursor = establish_backend()

    if not conn or not cursor:
        feedback_label.configure(text="Failed to establish backend connection.", text_color="red")
        return False

    try:
        query = "SELECT user_id, password, actions, admin_id FROM User WHERE username = '{}'".format(username)
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            user_id, stored_password, actions, admin_id = result

            if actions == 1:  # Account flagged
                cursor.execute("SELECT first_name, adminname FROM Admin WHERE admin_id = %s", (admin_id,))
                admin_info = cursor.fetchone()

                if admin_info:
                    admin_first_name, admin_username = admin_info
                    feedback_label.configure(
                        text=f"Account flagged. Contact admin: {admin_first_name} (Username: {admin_username})", 
                        text_color="red"
                    )
                else:
                    feedback_label.configure(
                        text="Account flagged. Contact your admin.", 
                        text_color="red"
                    )
                return False
            else:
                if entered_password == stored_password:  # Password matches
                    track_login_activity(user_id)
                    show_user_panel(root,user_id)
                else:  # Password incorrect
                    feedback_label.configure(text="Incorrect password. Please try again.", text_color="red")
                    return False
        else:  # Username does not exist
            feedback_label.configure(text="Username does not exist.", text_color="red")
            return False

    except Exception as e:
        feedback_label.configure(text=f"An error occurred: {e}", text_color="red")
        return False

    finally:
        conn.close()
