from Backend.establish_backend import establish_backend

def get_all_users_under_admin(admin_id):
    conn, cursor = establish_backend()
    if not conn or not cursor:
        print("Failed to establish backend connection.")
        return []

    try:
        query = """
            SELECT user_id, username, CONCAT(first_name, ' ', last_name) AS name, email, actions 
            FROM User 
            WHERE admin_id = %s
        """
        cursor.execute(query, (admin_id,))
        users = cursor.fetchall()
        return users  # This will return a list of tuples containing user details

    except Exception as e:
        print("An error occurred while fetching user data:", e)
        return []
    
    finally:
        conn.close()
