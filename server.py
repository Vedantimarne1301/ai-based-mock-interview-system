from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)  # Enable CORS that connects our express server

# Load variables from .env into environment
load_dotenv()

# API KEY configuration
#Access the variable
api_key=os.getenv("API_KEY")
# Make sure it's not None
if not api_key:
    raise ValueError("API_KEY not found in environment variables!")

# Configure the GenAI API
genai.configure(api_key=api_key)

# Function to Generate Interview Question
def generate_question(job_role, interview_type):
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = f"Generate a brief yet precise {interview_type} interview question for a {job_role}. Ensure the question is clear, focused, and requires a concise response. Avoid lengthy descriptions."
    response = model.generate_content(prompt)
    return response.text

# Function to Evaluate Answer and provide feedback
def evaluate_answer(question, answer):
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = (f"Here is an interview question: '{question}'. The candidate answered: '{answer}'. "
              "Provide a constructive feedback, ensure the feedback is clear, consice, and highlights both strengths and improvement points in 2-3 sentences.")
    response = model.generate_content(prompt)
    return response.text

# Function to Generate Follow-Up Question based on previous respinse
def generate_follow_up(question, answer):
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = (f"Based on the candidate's response: '{answer}', generate a highly relevant follow-up question "
              f"that digs deeper into their knowledge of the topic.")
    response = model.generate_content(prompt)
    return response.text

# API Route: Generate Question, recevies post request from express
@app.route('/generate-question', methods=['POST'])
def generate_question_api():
    try:
        data = request.get_json()
        job_role = data.get('job_role')
        interview_type = data.get('interview_type')

        #  Validate Input
        if not job_role or not interview_type:
            return jsonify({'error': 'Job role and interview type are required'}), 400

        question = generate_question(job_role, interview_type)
        return jsonify({'question': question})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API Route: Evaluate Answer based on user's response through post request
@app.route('/evaluate-answer', methods=['POST'])
def evaluate_answer_api():
    try:
        data = request.get_json()
        question = data.get('question')
        answer = data.get('answer')

        #  Validate Input
        if not question or not answer:
            return jsonify({'error': 'Question and answer are required'}), 400

        feedback = evaluate_answer(question, answer)
        return jsonify({'feedback': feedback})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API Route: Generate Follow-Up Question
@app.route('/generate-follow-up', methods=['POST'])
def generate_follow_up_api():
    try:
        data = request.get_json()
        question = data.get('question')
        answer = data.get('answer')

        #  Validate Input
        if not question or not answer:
            return jsonify({'error': 'Question and answer are required'}), 400

        follow_up_question = generate_follow_up(question, answer)
        return jsonify({'follow_up_question': follow_up_question})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask Application i.e backend server
app.run(host='0.0.0.0', port=5000, debug=True)
