# SECTION: TW21
# LEADER: Aerick Lee P. Alba
# MEMBERS:
# Cordero, Jose III
# De Guia, Jonash
# Lising, Romar 

from db import connect_db

def add_appointment(user_id, title, date, time):
    conn = connect_db()
    cursor = conn.cursor()

    query = "INSERT INTO appointments (user_id, title, date, time) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (user_id, title, date, time))

    conn.commit()
    conn.close()


def get_appointments(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM appointments WHERE user_id=%s", (user_id,))
    result = cursor.fetchall()

    conn.close()
    return result


def delete_appointment(app_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM appointments WHERE id=%s", (app_id,))
    conn.commit()
    conn.close()