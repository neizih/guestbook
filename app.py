import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
  app=app,
  key_func=get_remote_address,
  default_limits=["200 per day", "50 per hour"]
)

app.secret_key = os.environ.get('SECRET_KEY')

def get_db():
  return psycopg2.connect(
      host=os.environ.get('DB_HOST', 'localhost'),
      port=os.environ.get('DB_PORT', '5432'),
      dbname=os.environ.get('DB_NAME', 'guestbook'),
      user=os.environ.get('DB_USER', 'postgres'),
      password=os.environ.get('DB_PASSWORD', '')
  )

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/aboutes")
def aboutes():
  return render_template('aboutes.html')

@app.route("/")
@app.route("/index")
def index():
  entry_id = request.args.get('reply_to')
  con = get_db()
  cur = con.cursor()
  cur.execute("""SELECT entries.*, COUNT(responses.id) AS reply_count FROM entries LEFT JOIN responses ON entries.id =
responses.entry_id GROUP BY entries.id""")
  data = cur.fetchall()
  data = list(reversed(data))

  cur.execute("SELECT * FROM responses")
  all_responses = cur.fetchall()

  con.close()

  return render_template("index.html", datas=data, entry_id=entry_id, all_responses=all_responses)

@app.route('/add', methods=["POST"])
@limiter.limit("You have exceeded the permitted limit")
def add_entry():
  author = request.form['author']
  body = request.form['body']

  if len(body) > 250:
      flash("Your message is way too long!")
      return redirect('/')

  if len(author) > 30:
      flash("Your username is way too long!")
      return redirect('/')

  con = get_db()
  cur = con.cursor()
  cur.execute("INSERT INTO entries (author, body) VALUES (%s,%s)", (author, body))
  con.commit()
  con.close()

  return redirect("/")

@app.route('/addResponse', methods=["POST"])
def add_response():
  entry_id = request.form['id_entry']
  author = request.form['author']
  body = request.form['body']

  if len(author) > 30:
      flash("Your username is way too long!")
      return redirect('/')

  if len(body) > 250:
     flash("Your message is way too long!")
     return redirect('/')

  con = get_db()
  cur = con.cursor()
  cur.execute("INSERT INTO responses (author, body, entry_id) VALUES (%s,%s,%s)", (author, body, entry_id))
  con.commit()
  con.close()

  return redirect("/")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
