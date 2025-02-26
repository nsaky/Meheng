import pymysql

def establish_backend():
    try:
        conn = pymysql.connect(
                host='bswd2x35g4liozwrfwgi-mysql.services.clever-cloud.com',
                user='ua39skk7fpux9eqv',
                password='secret-password-removed-for-security',
                database='bswd2x35g4liozwrfwgi'
        )
        cursor = conn.cursor()


        # Create Admin Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Admin (
                admin_id VARCHAR(50) PRIMARY KEY,
                adminname VARCHAR(50) UNIQUE NOT NULL,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50),
                email VARCHAR(100) UNIQUE NOT NULL,
                phone INT(15),
                DOB DATE,
                address VARCHAR(255),
                password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            );
        ''')

        # Create User Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS User (
                user_id VARCHAR(50) PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50),
                email VARCHAR(100) UNIQUE NOT NULL,
                phone INT(15),
                DOB DATE,
                address VARCHAR(255),
                password VARCHAR(255) NOT NULL,
                admin_id VARCHAR(50) NOT NULL,
                actions TINYINT(1) DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (admin_id) REFERENCES Admin(admin_id)
            );
        ''')

        # Create Conversation Logs Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ConversationLogs (
                log_id INT PRIMARY KEY AUTO_INCREMENT,
                user_id VARCHAR(50) NOT NULL,
                query TEXT NOT NULL,
                response TEXT,
                is_objectionable TINYINT(1) DEFAULT 0,
                log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES User(user_id)
            );
        ''')

        # Create Admin Conversation Logs Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS AdminConversationLogs (
                log_id INT PRIMARY KEY AUTO_INCREMENT,
                admin_id VARCHAR(50) NOT NULL,
                query TEXT NOT NULL,
                response TEXT,
                is_objectionable TINYINT(1) DEFAULT 0,
                log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (admin_id) REFERENCES Admin(admin_id)
            );
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS LoginActivity (
                session_id INT PRIMARY KEY AUTO_INCREMENT,
                user_or_admin_id VARCHAR(50) NOT NULL,
                login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                ip_address VARCHAR(50)
            );
        ''')

        conn.commit()
        return conn, cursor

    except Exception as e:
        print("\nCan't establish backend connection:", e)
