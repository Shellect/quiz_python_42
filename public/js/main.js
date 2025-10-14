async function getNextQuestion() {
    let questionEl = document.querySelector('.question');
    let answersEl = document.querySelectorAll('.answer');
    let response = await fetch("/api/v1/question");
    let data = await response.json();
    questionEl.innerText = data.question;
    for (let index = 0; index < data.answers.length; index++) {
        answersEl[index].innerText = data.answers[index];
    }
}

getNextQuestion();