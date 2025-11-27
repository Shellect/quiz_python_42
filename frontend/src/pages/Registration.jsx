

export default function () {
    return (
        <div className="card box-shadow mt-4">
            <div className="card-title text-center mt-3">
                <h3>Создать аккаунт</h3>
                <span className="text-muted">Заполните форму для регистрации</span>
            </div>
            <div className="card-body">
                <form id="loginForm">
                      <div className="form-group mt-3">
                        <label htmlFor="username" className="form-label">User name:</label>
                        <input id="username" className="form-control" />
                        <span className="text-danger" id="authError"></span>
                    </div>
                    <div className="form-group mt-3">
                        <label htmlFor="userEmail" className="form-label">Email</label>
                        <input id="userEmail" type="email" className="form-control" />
                    </div>
                    <div className="form-group mt-3">
                        <label htmlFor="userPassword" className="form-label">Password</label>
                        <input id="userPassword" type="password" className="form-control" />
                    </div>
                    <div className="form-group mt-3">
                        <label htmlFor="confirmUserPassword" className="form-label">Confirm Password</label>
                        <input id="confirmUserPassword" type="password" className="form-control" />
                    </div>

                    <div className="d-grid mt-3">
                        <button id="loginBtn" className="btn btn-success">Register</button>
                    </div>
                </form>
            </div>
            <div className="card-footer">
                <p>Уже есть аккаунт? <a href="login.html">Войти</a></p>
            </div>
        </div>
    );
}