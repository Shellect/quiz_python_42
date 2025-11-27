import { NavLink } from "react-router";

export default function () {
    return (
        <nav className="navbar navbar-expand-lg bg-body-tertiary">
          <div className="container-fluid">
            <NavLink className="navbar-brand" to="/">Quiz</NavLink>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbar">
              <div className="navbar-nav">
                <NavLink className="nav-link active" to="/">Home</NavLink>
                <NavLink className="nav-link" to="/registration">Registration</NavLink>
              </div>
            </div>
          </div>
        </nav>
    );
}