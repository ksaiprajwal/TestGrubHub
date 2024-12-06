import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import './auth/LoginForm.css'; // Reuse the LoginForm styles

const AdminLogin = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const history = useHistory();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (email === 'test@gmail.com' && password === 'test1234') {
      history.push('/admin-dashboard');
    } else {
      setError('Invalid credentials');
    }
  };

  return (
    <>
      <div className='sign-up-header'>
        <h1>Admin Login</h1>
      </div>
      <div className="sign-up-form-wrapper">
        <div className="login-and-image">
          <form onSubmit={handleSubmit}>
            <div className="required-fields-text">
              {error && <div className='signup-error-text'>{error}*</div>}
            </div>
            <div id="input-space">
              <input
                id="login-email-input"
                name="email"
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div id="input-space">
              <input
                id="login-password-input"
                name="password"
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            <div id="button-space">
              <button id="login-submit-button" type="submit">
                Login
              </button>
            </div>
          </form>
        </div>
      </div>
    </>
  );
};

export default AdminLogin;