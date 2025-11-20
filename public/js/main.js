async function getUser() {
    const response = await fetch("/api/v1/auth/session_data", {
        headers: {
            "Content-Type": "application/json",
        },
        credentials: "include"
    });
    return await response.json();
}

async function getSession() {
        const user = await getUser();
        if (!user.session_data.is_authenticated) {
            window.location.href = '/login.html';
        } else {
            await getNextQuestion();
        }
}


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

getSession();