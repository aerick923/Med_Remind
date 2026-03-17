# SECTION: TW21
# LEADER: Aerick Lee P. Alba
# MEMBERS:
# Cordero, Jose III
# De Guia, Jonash
# Lising, Romar 

import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # PUT YOUR PASSWORD HERE
        database="medremind"
    )