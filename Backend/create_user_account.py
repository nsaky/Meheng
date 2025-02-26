import random
from Backend.establish_backend import establish_backend

def generate_unique_id(prefix, existing_ids):
    while True:
        random_number = int(random.random() * 10**16)
        unique_id = f"{prefix}{random_number}"
        if unique_id not in existing_ids:
            return unique_id
        else:
            generate_unique_id()


def get_all_username_email():
    conn, cursor = establish_backend()

    if not conn or not cursor:
        print("Failed to establish backend connection.")
        return [], []

    try:
        cursor.execute("SELECT username, email FROM User")
        user_data = cursor.fetchall()  # Fetch all usernames and emails
        
        usernames = [row[0] for row in user_data]  # Extract usernames
        emails = [row[1] for row in user_data]     # Extract emails

        return usernames, emails

    except Exception as e:
        print("Error occurred while fetching usernames and emails:", e)
        return [], []

    finally:
        cursor.close()
        conn.close()

def create_user_account(admin_id, username, first_name, last_name, email, phone, dob, address, password):
    conn, cursor = establish_backend()

    if not conn or not cursor:
        return None, False, "Failed to establish backend connection."

    try:
        cursor.execute("SELECT user_id FROM User")
        existing_user_ids = [row[0] for row in cursor.fetchall()]
        
        user_id = generate_unique_id("user", existing_user_ids)

        # Insert the new user record into the database, allowing NULL for non-compulsory fields
        cursor.execute('''
            INSERT INTO User (user_id, username, first_name, last_name, email, phone, DOB, address, password, admin_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (user_id, username, first_name, last_name, email, phone, dob, address, password, admin_id))

        conn.commit()
        return user_id, True, None  # Return user ID on success

    except Exception as e:
        return None, False, str(e)

    finally:
        cursor.close()
        conn.close()
