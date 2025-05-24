import express from 'express';
import bodyParser from 'body-parser';
import axios from 'axios';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const port = 3000;

app.set('view engine', 'ejs');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

const pythonApiUrl = 'http://127.0.0.1:5000'; // Python API URL

// Home Page (index.ejs)
app.get('/', (req, res) => {
    res.render('index');
});

// Handle Interview Type (Technical, Behavioral, System Design)
app.get('/:interview_type', (req, res) => {
    const interviewType = req.params.interview_type;
    res.render('interview', {
        interviewType: interviewType,
        question: null,
        feedback: null,
        followUp: null,
        answer: null
    });
});

// Start Interview (POST Method)
app.post("/start-interview", (req, res) => {
    const interviewType = req.body.interview_type;
    res.render("interview", {
        interviewType: interviewType,
        question: "", 
        feedback: "", 
        answer: ""
    });
});

//  Generate Question from Python API
app.post('/generate-question', async (req, res) => {
    const { job_role, interview_type } = req.body;
    try {
        const response = await axios.post(`${pythonApiUrl}/generate-question`, { job_role, interview_type });
        const question = response.data.question;

        res.render('interview', {
            interviewType: interview_type,
            question: question,
            feedback: null,
            followUp: null,
            answer: null
        });
    } catch (error) {
        console.error('Error generating question:', error);
        res.render('interview', {
            interviewType: interview_type,
            question: 'Failed to generate question',
            feedback: null,
            followUp: null,
            answer: null
        });
    }
});

// Evaluate Answer from Python API
app.post('/evaluate-answer', async (req, res) => {
    const { question, answer, interview_type } = req.body;
    if (!answer.trim()) {
        return res.render('interview', {
            interviewType: interview_type,
            question: question,
            feedback: ' Please provide an answer to proceed.',
            followUp: null,
            answer: answer
        });
    }

    try {
        const response = await axios.post(`${pythonApiUrl}/evaluate-answer`, { question, answer });
        const feedback = response.data.feedback;

        res.render('interview', {
            interviewType: interview_type,
            question: question,
            feedback: feedback,
            followUp: null,
            answer: answer
        });
    } catch (error) {
        console.error('Error evaluating answer:', error);
        res.render('interview', {
            interviewType: interview_type,
            question: question,
            feedback: 'Failed to evaluate answer',
            followUp: null,
            answer: answer
        });
    }
});

// Generate Follow-Up Question from Python API
app.post('/generate-follow-up', async (req, res) => {
    const { question, answer, interview_type } = req.body;
    if (!answer.trim()) {
        return res.render('interview', {
            interviewType: interview_type,
            question: question,
            feedback: ' Please answer the question before generating a follow-up.',
            followUp: null,
            answer: answer
        });
    }

    try {
        const response = await axios.post(`${pythonApiUrl}/generate-follow-up`, { question, answer });
        const followUp = response.data.follow_up_question;

        res.render('interview', {
            interviewType: interview_type,
            question: followUp,
            feedback: null,
            followUp: followUp,
            answer: ''
        });
    } catch (error) {
        console.error('Error generating follow-up question:', error);
        res.render('interview', {
            interviewType: interview_type,
            question: 'Failed to generate follow-up question',
            feedback: null,
            followUp: null,
            answer: answer
        });
    }
});

app.listen(port, () => {
    console.log(` Server running on port ${port}`);
});
