from database import connect

def register_user(name, username, password):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing = cursor.fetchone()

    if existing:
        print("Username already exists!")
        conn.close()
        return

    cursor.execute("""
    INSERT INTO users (name, username, password)
    VALUES (?, ?, ?)
    """, (name, username, password))

    conn.commit()
    conn.close()

    print("User registered successfully!")

def login_user(username, password):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM users WHERE username=? AND password=?
    """, (username, password))

    user = cursor.fetchone()
    conn.close()

    if user:
        print("Login successful!")
        return user[0]   # return user_id
    else:
        print("Invalid username or password!")
        return None