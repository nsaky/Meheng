from Backend.establish_backend import establish_backend

def admin_view_chats(admin_id, start_date=None, end_date=None):
    conn, cursor = establish_backend()

    if not conn or not cursor:
        print("Failed to establish backend connection.")
        return []

    try:
        if start_date and end_date:
            start_date = f"{start_date} 00:00:00"
            end_date = f"{end_date} 23:59:59"

            cursor.execute('''
                SELECT query, response, log_time FROM AdminConversationLogs
                WHERE admin_id = %s AND log_time BETWEEN %s AND %s
            ''', (admin_id, start_date, end_date))
        else:
            cursor.execute('''
                SELECT query, response, log_time FROM AdminConversationLogs WHERE admin_id = %s
            ''', (admin_id,))

        chats = cursor.fetchall()
        return chats if chats else []

    except Exception as e:
        print("An error occurred while fetching chat history:", e)
        return []

    finally:
        conn.close()
