import socket
from Backend.establish_backend import establish_backend

def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        print("Unable to get the IP address:", e)
        return None

def track_login_activity(user_or_admin_id):
    conn, cursor = establish_backend()

    if not conn or not cursor:
        print("Failed to establish backend connection.")
        return False

    try:
        ip_address = get_ip_address()

        if not ip_address:
            print("Could not detect IP address.")
            return False

        query = '''
            INSERT INTO LoginActivity (user_or_admin_id, ip_address)
            VALUES (%s, %s)
        '''
        cursor.execute(query, (user_or_admin_id, ip_address))
        conn.commit()

    except Exception as e:
        print("An error occurred while tracking login activity:", e)

    finally:
        cursor.close()
        conn.close()

