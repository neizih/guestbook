from flask import Flask, render_template, request, redirect,url_for, flash
import sqlite3 as sql 

app = Flask(__name__) 

@app.route("/") 
@app.route("/index") 
def index(): 
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM entries")
    data = cur.fetchall()
    con.close()

    print("Data", data) 
    print("Length", len(data))

    if not data: 
        return " No entries yet "

    return render_template("index.html", datas=data)

@app.route('/add', methods=["POST"])
def add_entry(): 
    author = request.form['author']
    body = request.form['body']

    con = sql.connect("database.db") 
    cur = con.cursor() 
    cur.execute("INSERT INTO entries (author, body) VALUES (?,?)", (author, body))
    con.commit() 
    con.close() 

    return redirect("/")
