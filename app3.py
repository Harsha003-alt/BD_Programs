from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,a
            email TEXT NOT NULL,
            age INTEGER
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/students', methods=['POST'])
def insert_student():
    data = request.get_json()
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO students (name, email, age) VALUES (?, ?, ?)',
        (data['name'], data['email'], data.get('age', 0))
    )
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    return jsonify({"message": "Student created", "id": student_id}), 201

@app.route('/students', methods=['GET'])
def get_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    conn.close()
    students = [
        {"id": r[0], "name": r[1], "email": r[2], "age": r[3]}
        for r in rows
    ]
    return jsonify(students)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

