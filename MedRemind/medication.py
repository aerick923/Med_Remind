# SECTION: TW21
# LEADER: Aerick Lee P. Alba
# MEMBERS:
# Cordero, Jose III
# De Guia, Jonash
# Lising, Romar 

from db import connect_db

def add_med(user_id, name, dosage, time):
    conn = connect_db()
    cursor = conn.cursor()

    query = "INSERT INTO medications (user_id, name, dosage, time) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (user_id, name, dosage, time))

    conn.commit()
    conn.close()


def get_meds(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM medications WHERE user_id=%s"
    cursor.execute(query, (user_id,))

    result = cursor.fetchall()
    conn.close()

    return result


def delete_med(med_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM medications WHERE id=%s", (med_id,))
    conn.commit()
    conn.close()