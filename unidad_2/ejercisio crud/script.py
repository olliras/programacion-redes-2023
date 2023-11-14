import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crud.db')  # Cambia el nombre del archivo de la base de datos si es diferente
    conn.row_factory = sqlite3.Row
    return conn

# Método GET donde busca un nombre
@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM equipo_futbol')
    data = cursor.fetchall()
    for reg in data:
       registros.append(dict(reg))
    conn.close()
    return jsonify(json.dumps(registros))

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO equipo_futbol (name, email, position, age, nationality) VALUES (?, ?, ?, ?, ?)'
    cursor.execute(insert, [record['name'], record['email'], record['position'], record['age'], record['nationality']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE equipo_futbol SET email = ?, age = ? WHERE name = ?'
    cursor.execute(update, [record['email'], record['age'], record['name']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM equipo_futbol WHERE name = ?'
    cursor.execute(delete, [record['name']])
    conn.commit()
    return jsonify(record)

if __name__ == '__main__':
    app.run(debug=True)
