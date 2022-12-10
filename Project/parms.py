import sqlite3

global db
global cursor
db = sqlite3.connect("server.db")
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    balance BIGINT,
    save BIGINT
)""")
db.commit()
