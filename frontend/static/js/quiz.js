// Get DOM elements
const quizContainer = document.getElementById('quiz-container');
const submitButton = document.getElementById('submit-button');
const nextButton = document.getElementById('next-button');
const resultDiv = document.getElementById('result');
const progressDiv = document.getElementById('progress');

// Initialize quiz index, user answers, and total quizzes
let quizIndex = 0;
let userAnswers = {};
let totalQuizzes = 0;

// Fetch total quizzes from backend
fetch('/quiz/total')
    .then(response => response.json())
    .then(data => {
        totalQuizzes = data.total;

        // Load first quiz from backend
        loadQuiz(quizIndex);
    });

function loadQuiz(index) {
    // Clear quiz container
    quizContainer.innerHTML = '';

    // Update progress
    progressDiv.textContent = 'Question ' + (index + 1) + ' of ' + totalQuizzes;

    // Load quiz from backend
    fetch('/quiz/' + index)
        .then(response => response.json())
        .then(quiz => {
            // Display quiz on page
            const questionDiv = document.createElement('div');
            questionDiv.className = 'question';
            questionDiv.textContent = quiz.question;

            const optionsUl = document.createElement('ul');
            optionsUl.className = 'options';

            for (let option of quiz.options) {
                const li = document.createElement('li');
                const label = document.createElement('label');
                const radio = document.createElement('input');
                radio.type = 'radio';
                radio.name = quiz.question;
                radio.value = option;
                label.appendChild(radio);
                label.appendChild(document.createTextNode(option));
                li.appendChild(label);
                optionsUl.appendChild(li);
            }

            questionDiv.appendChild(optionsUl);
            quizContainer.appendChild(questionDiv);

            // Increment quiz index and update buttons
            quizIndex++;
            if (quizIndex >= totalQuizzes) {
                nextButton.style.display = 'none';
                submitButton.style.display = 'block';
            }
        });
}

// Handle next button click
nextButton.addEventListener('click', () => {
    // Collect user's answer
    const userAnswer = document.querySelector('input[type=radio]:checked').value;
    userAnswers[quizIndex - 1] = userAnswer;  // Use quizIndex - 1 because quizIndex was already incremented in loadQuiz

    // Load next quiz
    if (quizIndex < totalQuizzes) {
        loadQuiz(quizIndex);
    }
});

// Handle submit button click
submitButton.addEventListener('click', () => {
    // Collect user's answer for the last question
    const userAnswer = document.querySelector('input[type=radio]:checked').value;
    userAnswers[quizIndex - 1] = userAnswer;  // Use quizIndex - 1 because quizIndex was already incremented in loadQuiz

    // Send user's answers to backend
    fetch('/quiz/check_answers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userAnswers)
    })
        .then(response => response.json())
        .then(result => {
            // Display result
            resultDiv.textContent = 'You got ' + result.correct_count + ' correct answers.';
        });
});
