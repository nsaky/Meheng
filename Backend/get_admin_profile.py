from Backend.establish_backend import establish_backend

def get_admin_profile(admin_id):
    conn, cursor = establish_backend()
    if not conn or not cursor:
        return None
    
    try:
        query = "SELECT * FROM Admin WHERE admin_id = %s"
        cursor.execute(query, (admin_id,))
        admin_profile = cursor.fetchone()
        return admin_profile  # Returns a tuple with admin details

    except Exception as e:
        print(f"Error fetching admin profile: {e}")
        return None

    finally:
        conn.close()