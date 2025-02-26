from Backend.establish_backend import establish_backend

def get_login_activities(admin_id, user_id):
    conn, cursor = establish_backend()
    if not conn or not cursor:
        return "Failed to establish connection.", []

    try:
        # Check if user exists and is controlled by this admin
        query_check_user = """
        SELECT COUNT(*) FROM User WHERE user_id = %s AND admin_id = %s
        """
        cursor.execute(query_check_user, (user_id, admin_id))
        user_exists = cursor.fetchone()[0]

        if user_exists == 0:
            return "User does not exist or is not controlled by this admin.", []

        # Fetch login activities for the user
        query_login_activities = """
        SELECT session_id, login_time, ip_address 
        FROM LoginActivity 
        WHERE user_or_admin_id = %s
        ORDER BY login_time DESC
        """
        cursor.execute(query_login_activities, (user_id,))
        login_activities = cursor.fetchall()

        return None, login_activities

    except Exception as e:
        print("Error:", e)
        return "An error occurred while fetching login activities.", []

    finally:
        conn.close()
