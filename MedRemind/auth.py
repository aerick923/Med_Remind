# SECTION: TW21
# LEADER: Aerick Lee P. Alba
# MEMBERS:
# Cordero, Jose III
# De Guia, Jonash
# Lising, Romar 

from db import connect_db

def register_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))

    conn.commit()
    conn.close()


def login_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    user = cursor.fetchone()
    conn.close()

    return user