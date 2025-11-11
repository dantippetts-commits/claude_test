from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

# Use /tmp for Vercel (ephemeral), local path for development
DATABASE = os.path.join('/tmp', 'todo.db') if os.environ.get('VERCEL') else 'todo.db'

# Track if database is initialized
_db_initialized = False

def init_db():
    """Initialize the database with the todos table"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    """Get a database connection"""
    global _db_initialized
    if not _db_initialized:
        init_db()
        _db_initialized = True

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/todos', methods=['GET'])
def get_todos():
    """Get all todos"""
    conn = get_db_connection()
    todos = conn.execute('SELECT * FROM todos ORDER BY created_at DESC').fetchall()
    conn.close()

    return jsonify([dict(row) for row in todos])

@app.route('/api/todos', methods=['POST'])
def add_todo():
    """Add a new todo"""
    data = request.get_json()
    task = data.get('task', '').strip()

    if not task:
        return jsonify({'error': 'Task cannot be empty'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO todos (task) VALUES (?)', (task,))
    conn.commit()
    todo_id = cursor.lastrowid
    conn.close()

    return jsonify({'id': todo_id, 'task': task, 'completed': 0}), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update a todo (mark as complete/incomplete or edit task)"""
    data = request.get_json()
    conn = get_db_connection()

    if 'completed' in data:
        conn.execute('UPDATE todos SET completed = ? WHERE id = ?',
                    (data['completed'], todo_id))

    if 'task' in data:
        task = data['task'].strip()
        if not task:
            conn.close()
            return jsonify({'error': 'Task cannot be empty'}), 400
        conn.execute('UPDATE todos SET task = ? WHERE id = ?',
                    (task, todo_id))

    conn.commit()
    todo = conn.execute('SELECT * FROM todos WHERE id = ?', (todo_id,)).fetchone()
    conn.close()

    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404

    return jsonify(dict(todo))

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    conn = get_db_connection()
    conn.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Todo deleted'}), 200

if __name__ == '__main__':
    # For local development only
    init_db()
    _db_initialized = True
    app.run(debug=True, port=5000)

# For Vercel deployment - the app object is automatically detected
