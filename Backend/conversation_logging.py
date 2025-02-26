from Backend.establish_backend import establish_backend

def conversation_logs(user_id, query, response):
    # List of objectionable words
    objectionable_words = ["suicide", "murder", "violence", "terrorist", "bomb", "drugs", "weapon", "assault", "kill", "rape", "abuse", "harassment", "threat", "kidnap", "arson", "stab", "hostage", "extortion", "explosive", "shoot", "homicide", "genocide", "lynching", "torture", "war", "massacre", "riot", "smuggle", "trafficking", "poison", "molestation", "slavery", "pedophile", "racism", "xenophobia", "vandalism", "terror", "mass shooting", "execute", "strangle", "behead", "aggression", "hatred", "homophobia", "transphobia", "radicalism", "propaganda", "anarchy", "sabotage", "cruelty"]

    is_objectionable = any(word in query.lower() for word in objectionable_words)
    
    conn, cursor = establish_backend()
    if not conn or not cursor:
        print("Database connection failed.")
        return False
    
    try:
        cursor.execute('''
            INSERT INTO ConversationLogs (user_id, query, response, is_objectionable)
            VALUES (%s, %s, %s, %s)
        ''', (user_id, query, response, int(is_objectionable)))

        conn.commit()

        if is_objectionable:
            cursor.execute('''
                SELECT COUNT(*) FROM ConversationLogs
                WHERE user_id = %s AND is_objectionable = 1
            ''', (user_id,))
            
            objectionable_count = cursor.fetchone()[0]

            if objectionable_count >= 10:
                cursor.execute('''
                    UPDATE User
                    SET actions = 1
                    WHERE user_id = %s
                ''', (user_id,))
                conn.commit()
                print(f"User {user_id} has been flagged for objectionable content.")
                exit()

    except Exception as e:
        print("Error logging conversation or updating user:", e)
    finally:
        conn.close()

