const loginForm = document.querySelector('#loginForm');
const loginBtn = document.getElementById('loginBtn');
const authError = document.getElementById('authError');
const userEmail = document.getElementById('userEmail');
const userPassword = document.getElementById('userPassword');
const confirmUserPassword =  document.getElementById('confirmUserPassword');

loginForm.addEventListener('submit', async function(e) {
    e.preventDefault();

    loginBtn.classList.remove('btn-success');
    loginBtn.classList.add('btn-secondary');
    loginBtn.setAttribute('disabled', true);

    authError.innerText = '';

    try {
        const response = await fetch('/api/v1/registration', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: userEmail.value,
                password: userPassword.value,
                confirmPassword: confirmUserPassword.value
            })
        });
        const data = await response.json();
        if (data.status === 'success') {
            setTimeout(() => {
                window.location.href = 'index.html';
            });
        } else {
            authError.innerText = data.detail;
        }
    } catch (error) {
        authError.innerText = 'Ошибка сети. Попробуйте позже';
        console.error(error)
    } finally {
        loginBtn.classList.remove('btn-secondary');
        loginBtn.classList.add('btn-success');
        loginBtn.removeAttribute('disabled');
    }
});