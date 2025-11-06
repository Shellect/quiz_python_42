function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : null;
}

async function getUser(session_id) {

}

async function getSession() {
    const session = getCookie('session_id');
    if (!session) {
        window.location.href = '/login.html';
    } else {
        const user = await getUser(session);
        if (!user) {
            window.location.href = '/login.html';
        } else {
            await getNextQuestion();
        }
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