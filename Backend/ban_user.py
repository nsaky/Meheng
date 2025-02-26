from Backend.establish_backend import establish_backend

def ban_user(admin_id, user_id):
    conn, cursor = establish_backend()

    if not conn or not cursor:
        return False, "Failed to establish backend connection."

    try:
        # Check if user exists
        cursor.execute('SELECT admin_id FROM User WHERE user_id = %s', (user_id,))
        result = cursor.fetchone()

        if not result:
            return False, "User does not exist."

        # Check if admin IDs match
        user_admin_id = result[0]
        if user_admin_id != admin_id:
            return False, "You are not authorized to ban this user."

        # Ban the user (set actions to 1)
        cursor.execute('UPDATE User SET actions = 1 WHERE user_id = %s', (user_id,))
        conn.commit()

        return True, f"User {user_id} has been banned successfully."

    except Exception as e:
        return False, f"An error occurred while banning user {user_id}: {e}"

    finally:
        conn.close()
