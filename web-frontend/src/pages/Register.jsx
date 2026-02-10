
import { useState } from "react";
import { registerUser } from "../services/api";
import { Link, useNavigate } from "react-router-dom";
import "../styles/Login.css"; // Shared CSS for visual consistenc.

const Register = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isProcessing, setIsProcessing] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsProcessing(true);

    try {
      await registerUser({
        username,
        email,
        password,
      });

      alert("Registration successful. Please login.");
      navigate("/login");
    } catch (error) {
      console.error("REGISTER ERROR:", error.response?.data);
      alert(
        error.response?.data?.error ||
          JSON.stringify(error.response?.data) ||
          "Registration failed"
      );
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <div className="auth-page-container">
      {/* Visual background layers */}
      <div className="background-grid"></div>
      <div className="background-glow"></div>

      <div className="auth-card">
        <header className="auth-header">
          <div className="brand-hexagon">⬢</div>
          <h1 className="auth-title">Register</h1>
          <p className="auth-subtitle">Create your analytics workstation profile</p>
        </header>

        <form onSubmit={handleSubmit} className="auth-form">
          <div className="input-group">
            <label>Username</label>
            <input
              type="text"
              placeholder="Pick a username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>

          <div className="input-group">
            <label>Email</label>
            <input
              type="email"
              placeholder="operator@company.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="input-group">
            <label>Password</label>
            <input
              type="password"
              placeholder="Minimum 8 characters"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          <button 
            type="submit" 
            className="btn-primary" 
            disabled={isProcessing}
          >
            {isProcessing ? "Processing..." : "Create Account"}
          </button>
        </form>

        <footer className="auth-footer">
          <Link to="/login" className="auth-link">
            Already have an account? <span className="highlight">Login</span>
          </Link>
        </footer>
      </div>

      <div className="terminal-info">
        <span>ENCRYPTED REGISTRATION</span>
        <span className="blink">_</span>
      </div>
    </div>
  );
};

export default Register;
