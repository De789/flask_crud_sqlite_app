from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = 'many random bytes'

DB_NAME = "crud.db"
import sqlite3

conn = sqlite3.connect("crud.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

@app.route('/show')
def show():
    conn = sqlite3.connect("crud.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return "<br>".join([f"{row['id']} - {row['name']} - {row['email']} - {row['phone']}" for row in rows])

# Helper function: connect to DB
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # To access columns by name
    return conn

# Initialize DB & table
with get_db_connection() as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)
    conn.commit()

@app.route('/')
def Index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    conn.close()
    return render_template('index.html', students=data)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        conn = get_db_connection()
        conn.execute("INSERT INTO students (name, email, phone) VALUES (?, ?, ?)", 
                     (name, email, phone))
        conn.commit()
        conn.close()

        flash("Data Inserted Successfully")
        return redirect(url_for('Index'))

@app.route('/delete/<int:id_data>', methods=['GET'])
def delete(id_data):
    conn = get_db_connection()
    conn.execute("DELETE FROM students WHERE id = ?", (id_data,))
    conn.commit()
    conn.close()

    flash("Record Has Been Deleted Successfully")
    return redirect(url_for('Index'))

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        conn = get_db_connection()
        conn.execute("""
            UPDATE students 
            SET name = ?, email = ?, phone = ?
            WHERE id = ?
        """, (name, email, phone, id_data))
        conn.commit()
        conn.close()

        flash("Data Updated Successfully")
        return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)
