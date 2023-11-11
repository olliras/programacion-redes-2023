import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Método GET donde busca un nombre
@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()

    if name:
        cursor.execute('SELECT * FROM equipo_futbol WHERE name = ?', (name,))
    else:
        cursor.execute('SELECT * FROM equipo_futbol')

    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(json.dumps(registros))

def get_db_connection():
    conn = sqlite3.connect('crud.db')  
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == '__main__':
    app.run(debug=True)
