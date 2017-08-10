from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')

@app.route('/')
def index():
	query = "SELECT * FROM users "                          
	friends = mysql.query_db(query)
	return render_template('index.html', all_friends = friends)


@app.route('/friends', methods=['POST'])
def create():

    query = "INSERT INTO users (name, age, created_at) VALUES (:name, :age, NOW())"

    data = {
             'name': request.form['name'],
             'age':  request.form['age'],

           }

    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)