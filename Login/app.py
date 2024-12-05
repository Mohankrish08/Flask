# importing libraries
from flask import render_template, jsonify, request, Flask, redirect
import sqlite3
import pandas as pd 
import os 

app = Flask(__name__)


# api calls
@app.route('/')
def index():
    return render_template('index.html')

# getting login creditals
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if data:
        print(f"Data: {data}")

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'username and password are required'}), 400
    
    query = f"SELECT * FROM LOGIN WHERE Email = ? and Password = ?";

    try:
        conn = sqlite3.connect('login-items.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query, (username, password))
        rows = cursor.fetchall()
        if rows:
            user_data = [dict(row) for row in rows]
            return jsonify({
                    "message": "Data in the Database!",
                    "code": 200,
                    }), 200
        elif rows == []:
            print("No data, kindly Sign Up!")
            return jsonify({"message": "No data in the Database", "code": 400}), 400
            
        conn.close()

    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal server error'}),500



if __name__ == "__main__":
    app.run(debug=True, port=5000)
