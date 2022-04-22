from sqlite3 import Cursor
from flask import Flask, render_template, request, redirect, session
import psycopg2
from sentiments import second
import os
app = Flask(__name__)

#init user cookie
app.secret_key = os.urandom(24)

#blueprint to call second python file in the project
app.register_blueprint(second)

#establishing a connection with postgresql database
try:    
    conn = psycopg2.connect(
        host="localhost",
        database="ekkirinaldi",
        user="ekkirinaldi",
        password=''
    )
    #Open a cursor to perform database operation
    cursor = conn.cursor()
except:
    print("An exception occured")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')    

@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    cursor.execute(
        "SELECT * from users WHERE email LIKE '{}' AND password LIKE '{}'".format(email, password))
    users = cursor.fetchall()
    # check if a user has already logged in
    if len(users) > 0:
        session['user_id'] = users[0][0]
        return redirect('/home')
    else:
        return redirect('/login')

@app.route('/add_user', methods=['POST'])
def add_user():

  # get user login data and pass the data to database
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')
    cursor.execute('INSERT INTO users (name, email, password)'
            'VALUES (%s, %s, %s)',
            (name, email, password,))
    conn.commit()
    cursor.execute(
        "SELECT * from users WHERE email LIKE '{}'".format(email))
    myuser = cursor.fetchall()
    session['user_id'] = myuser[0][0]
    return redirect('/home')
 
 
@app.route('/logout')
def logout():
  # close the session
    session.pop('user_id')
    return redirect('/')
 
 
if __name__ == "__main__":
    app.run(debug=True)
