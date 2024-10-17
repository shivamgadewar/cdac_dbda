from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup
def init_db():
    with sqlite3.connect('library.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
        conn.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER)')

# Route for Home
@app.route('/')
def index():
    return render_template('index.html')

# Route for Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('library.db') as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
            user = cur.fetchone()
            if user:
                session['user_id'] = user[0]
                return redirect(url_for('display_books'))
            else:
                return "Invalid username or password"
    return render_template('login.html')

# Route for displaying books
@app.route('/books')
def display_books():
    with sqlite3.connect('library.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM books')
        books = cur.fetchall()
    return render_template('books.html', books=books)

# Route for adding books
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        with sqlite3.connect('library.db') as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', (title, author, year))
            conn.commit()
        return redirect(url_for('display_books'))
    return render_template('base.html')

# Initialize the database
init_db()

if __name__ == '__main__':
    app.run(debug=True)
