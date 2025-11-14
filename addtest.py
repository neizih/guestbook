import sqlite3 as sql 

con = sql.connect('database.db') 
cur = con.cursor() 

cur.execute("INSERT INTO entries (author, body) VALUES (?,?)", ("Nazih", "Hello this is a test")) 

con.commit() 
con.close()
print("Data Added") 
