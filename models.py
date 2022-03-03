import sqlite3

conn = sqlite3.connect('database.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS data(
   name TEXT, 
   username TEXT,
   password TEXT,
   description TEXT);
""")
conn.commit()

