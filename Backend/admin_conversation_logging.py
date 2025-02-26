from Backend.establish_backend import establish_backend

def admin_conversation_logs(admin_id, query, response):
    # List of objectionable words
    objectionable_words = ["suicide", "murder", "violence", "terrorist", "bomb", "drugs", "weapon", "assault", "kill", "rape", "abuse", "harassment", "threat", "kidnap", "arson", "stab", "hostage", "extortion", "explosive", "shoot", "homicide", "genocide", "lynching", "torture", "war", "massacre", "riot", "smuggle", "trafficking", "poison", "molestation", "slavery", "pedophile", "racism", "xenophobia", "vandalism", "terror", "mass shooting", "execute", "strangle", "behead", "aggression", "hatred", "homophobia", "transphobia", "radicalism", "propaganda", "anarchy", "sabotage", "cruelty"]

    is_objectionable = any(word in query.lower() for word in objectionable_words)
    
    conn, cursor = establish_backend()
    if not conn or not cursor:
        print("Database connection failed.")
        return False
    
    try:
        cursor.execute('''
            INSERT INTO AdminConversationLogs (admin_id, query, response, is_objectionable)
            VALUES (%s, %s, %s, %s)
        ''', (admin_id, query, response, int(is_objectionable)))

        conn.commit()


    except Exception as e:
        print("Error logging conversation", e)
    finally:
        conn.close()

