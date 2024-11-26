import numpy as np 
import pandas as pd 
import os 
from flask import Flask, render_template, jsonify, request, session, redirect, url_for
import time

app = Flask(__name__)
# app.secret_key = "49b1a43fcc78357f0df8ff8a3ad6c188"
SESSION_TIMEOUT = 5 *60
WARNING_TIME = 4 * 60

df = pd.read_csv('./cricket.csv')


@app.before_request
def check_session():

    if 'start_time' not in session:
        session['start_time'] = time.time()
    session_duration = time.time() - session['start_time']

    if session_duration > SESSION_TIMEOUT:
        return redirect(url_for('session_expired!'))
    
@app.route('/extend_session', methods=['POST'])
def extend_session():
    session['start_time'] = time.time()
    return jsonify({'message': 'session extended!!'})

@app.route('/')
def index():
    # Convert DataFrame to a nested dictionary
    questions = {}
    for _, row in df.iterrows():
        q_id = row['question_id']
        if q_id not in questions:
            questions[q_id] = {
                'question_text': row['question_text'],
                'options': {}
            }
        o_id = row['option_id']
        if o_id not in questions[q_id]['options']:
            questions[q_id]['options'][o_id] = {
                'option_text': row['option_text'],
                'sub_options': []
            }
        questions[q_id]['options'][o_id]['sub_options'].append({
            'sub_option_id': row['sub_option_id'],
            'sub_option_text': row['sub_option_text']
        })

    return render_template('index.html', questions=questions)


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    df_new = pd.DataFrame(data)
    print("*" * 30)
    print(df_new)

    return jsonify({"message": "Data received!", "data": data})


if __name__ == "__main__":
    app.run(debug=True)