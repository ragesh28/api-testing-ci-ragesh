from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('data.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    return conn

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    conn = get_db()
    conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (data['name'], data['email']))
    conn.commit()
    return jsonify({'message': 'User created'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM users")
    users = [{'id': row[0], 'name': row[1], 'email': row[2]} for row in cursor]
    return jsonify(users)

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    conn = get_db()
    conn.execute("UPDATE users SET name=?, email=? WHERE id=?", (data['name'], data['email'], id))
    conn.commit()
    return jsonify({'message': 'User updated'})

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_db()
    conn.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    return jsonify({'message': 'User deleted'})

if __name__ == '__main__':
    app.run(debug=True)
