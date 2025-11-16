import sqlite3 as sql

con = sql.connect('database.db')
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS entries")
cur.execute("DROP TABLE IF EXISTS responses")

create_entries = '''CREATE TABLE "entries"(
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "author" TEXT NOT NULL,
        "body" TEXT NOT NULL,
        "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )'''

create_responses = '''CREATE TABLE "responses"(
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "entry_id" INTEGER NOT NULL,
        "author" TEXT NOT NULL,
        "body" TEXT NOT NULL,
        "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (entry_id) REFERENCES entries(id)
        )'''

cur.execute(create_entries)
cur.execute(create_responses)
con.commit()
con.close()
print("Tables created!")
