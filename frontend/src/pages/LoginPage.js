import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import AuthContext from '../context/AuthContext';
import './LoginPage.css'; // Import the new CSS file

const LoginPage = () => {
  const { loginUser } = useContext(AuthContext);

  return (
    <div className="Auth-form-container">
      <form className="Auth-form" onSubmit={loginUser}>
        <div className="Auth-form-content">
          <h2 className="Auth-form-title">Login</h2>
          <div className="form-group">
            <label>Username</label>
            <input type="text" name="username" placeholder="Enter Username" className="note" />
          </div>
          <div className="form-group">
            <label>Password</label>
            <input type="password" name="password" placeholder="Enter Password" className="note" />
          </div>
          <button className="btn btn-primary">SignIn</button>
          <p>
            Don't have an account? <Link to="/signup">Sign Up</Link>
          </p>
        </div>
      </form>
    </div>
  );
};

export default LoginPage;
