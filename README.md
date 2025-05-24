#  AI-Based Mock Interview System

An AI-powered mock interview platform designed to simulate real interview experiences. The system evaluates answers, provides instant feedback,a holistic performance score.

##  Features

-  **Interview Type Selection** – Choose interview categories like Technical, HR, or Behavioral.
-  **AI-Powered Questioning** – Dynamic and adaptive questions generated using Natural Language Processing (NLP).
-  **Answer Evaluation** – Automatically evaluates responses for content quality, relevance, and clarity.
-  **Performance Scoring** – Score based on correctness, fluency, and AI-generated feedback.
-  **Follow-Up Questions** – AI-generated follow-ups based on your previous answers.
-  **Detailed Report** – Performance summary with scores and suggestions for improvement.

##  Tech Stack

### Frontend
- HTML, CSS, JavaScript

###  Backend
- Python (Flask / FastAPI)
- Gemini API (for question generation and evaluation)

---

##  Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-mock-interview.git
cd ai-mock-interview
```

### 2. Set up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add OpenAI API Key
Create a `.env` file in the root directory:
```
API_KEY= YOUR_API_KEY
```

### 5. Run the Application
```bash
python server/app.py
nodemon index.js
```
then visit localhost3000 on your browser

---

##  Future Enhancements

- Voice input and sentiment analysis
- Multi-language support
- Resume parsing for personalized interviews
- Cloud deployment (Heroku / Render / AWS)
- Facial Expression recognition

##  License

This project is licensed under the MIT License. Feel free to use, modify, and distribute.
