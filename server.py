from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends_appdb')

@app.route('/')
def index():
    query = "SELECT name, age, DATE_FORMAT(friends.created_at,'%M %d') as date,DATE_FORMAT(friends.created_at,'%Y') as year  FROM friends"                           # define your query
    friends = mysql.query_db(query)# run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template

@app.route('/add_friend', methods=['POST'])
def add_friend():
    query = "INSERT INTO friends (name, age, created_at, updated_at) VAlUES(:name, :age, NOW(), NOW())"
    data = {
        "name": request.form["f_name"],
        "age": request.form["age"]
    }
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
