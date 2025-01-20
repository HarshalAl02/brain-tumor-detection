import mysql.connector
from fuzzywuzzy import process
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='chatbot_db'
    )

def get_response_from_db(user_input):
    conn = get_db_connection()
    cursor = conn.cursor()

    user_input = user_input.lower().strip()
    cursor.execute("SELECT user_input, bot_response FROM chatbot_responses")
    responses = cursor.fetchall()

    inputs = [response[0].lower() for response in responses]

    if user_input in inputs:
        for db_input, bot_response in responses:
            if db_input.lower() == user_input:
                conn.close()
                return bot_response

    best_match, score = process.extractOne(user_input, inputs)

    if score > 80:
        for db_input, bot_response in responses:
            if db_input.lower() == best_match:
                conn.close()
                return bot_response
    else:
        conn.close()
        return "I'm sorry, I didn't understand that."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def get_bot_response():
    user_input = request.args.get('msg')
    bot_response = get_response_from_db(user_input)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
