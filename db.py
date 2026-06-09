import os
import psycopg2

con = psycopg2.connect(
  host=os.environ.get('DB_HOST', 'localhost'),
  port=os.environ.get('DB_PORT', '5432'),
  dbname=os.environ.get('DB_NAME', 'guestbook'),
  user=os.environ.get('DB_USER', 'postgres'),
  password=os.environ.get('DB_PASSWORD', '')
)
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS entries (
  id SERIAL PRIMARY KEY,
  author TEXT NOT NULL,
  body TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS responses (
  id SERIAL PRIMARY KEY,
  entry_id INTEGER NOT NULL REFERENCES entries(id),
  author TEXT NOT NULL,
  body TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')

con.commit()
con.close()
print("Tables created!")

