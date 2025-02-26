from Backend.establish_backend import establish_backend

def get_objectionable_chats(user_id):
    conn, cursor = establish_backend()

    if not conn or not cursor:
        print("Failed to establish backend connection.")
        return []

    try:
        cursor.execute("SELECT query, response, log_time FROM ConversationLogs WHERE user_id = %s AND is_objectionable = 1", (user_id,))
        return cursor.fetchall()
    except Exception as e:
        print("An error occurred while fetching objectionable chats:", e)
        return []
    finally:
        conn.close()

