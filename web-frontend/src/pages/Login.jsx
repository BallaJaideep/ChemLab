
import { useState } from "react";
import { loginUser } from "../services/api";
import { setToken } from "../services/auth";
import { Link, useNavigate } from "react-router-dom";
import "../styles/Login.css";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isAuthenticating, setIsAuthenticating] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsAuthenticating(true);
    try {
      const data = await loginUser({ username, password });
      setToken(data.access);
      navigate("/");
    } catch {
      alert("Access Denied: Invalid Username or Password");
    } finally {
      setIsAuthenticating(false);
    }
  };

  return (
    <div className="auth-page-container">
      {/* Complex layered background */}
      <div className="background-grid"></div>
      <div className="background-glow"></div>

      <div className="auth-card">
        <header className="auth-header">
          <div className="brand-hexagon">⬢</div>
          <h1 className="auth-title">System Access</h1>
          <p className="auth-subtitle">Chemical Equipment Analytics Portal</p>
        </header>

        <form onSubmit={handleSubmit} className="auth-form">
          <div className="input-group">
            <label>Username</label>
            <input
              type="text"
              placeholder="Enter your username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>

          <div className="input-group">
            <label>Password</label>
            <input
              type="password"
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          <button 
            type="submit" 
            className="btn-primary" 
            disabled={isAuthenticating}
          >
            {isAuthenticating ? "Authenticating..." : "Authorize Access"}
          </button>
        </form>

        <footer className="auth-footer">
          <Link to="/register" className="auth-link">
            New Operator? <span className="highlight">Initialize Account</span>
          </Link>
          <div className="footer-separator"></div>
          <Link to="/forgot-password" id="forgot-pass" className="auth-link secondary">
            Forgot Password?
          </Link>
        </footer>
      </div>

      <div className="terminal-info">
        <span>STABLE CONNECTION</span>
        <span className="blink">_</span>
      </div>
    </div>
  );
};

export default Login;
