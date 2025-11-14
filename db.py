import sqlite3 as sql 

# connects to sqlite
con = sql.connect('database.db') 

# creates a connection
cur = con.cursor() 

#drops table if already exists
cur.execute("DROP TABLE IF EXISTS entries") 
cur.execute("DROP TABLE IF EXISTS response") 

# create entries table id database.db
create_table = '''CREATE TABLE "entries"(
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "author" TEXT NOT NULL,
        "body" TEXT NOT NULL, 
        "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        "responses" INTEGER,
        )'''

create_response_table = '''CREATE TABLE "entries"(
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "author" TEXT NOT NULL,
        "body" TEXT NOT NULL, 
        "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )'''


cur.execute(create_table) 

con.commit() 

con.close()
