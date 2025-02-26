from Backend.establish_backend import establish_backend

def get_user_profile(user_id):
    conn, cursor = establish_backend()
    if not conn or not cursor:
        return None
    
    try:
        query = "SELECT * FROM User WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        user_profile = cursor.fetchone()
        return user_profile  # Returns a tuple with user details

    except Exception as e:
        print(f"Error fetching user profile: {e}")
        return None

    finally:
        conn.close()