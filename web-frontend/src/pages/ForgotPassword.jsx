
import { useState } from "react";
import { Link } from "react-router-dom";
import api from "../services/api";
import "../styles/Login.css"; // keep your enterprise styling

const ForgotPassword = () => {
  const [email, setEmail] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      await api.post("auth/forgot-password/", { email });
      setSubmitted(true);
    } catch  {
      alert("Unable to process request. Try again later.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-page-container">
      {/* Complex industrial background layers */}
      <div className="background-grid"></div>
      <div className="background-glow"></div>

      <div className="auth-card">
        <header className="auth-header">
          <div className="brand-hexagon">⬢</div>
          <h1 className="auth-title">Reset Password</h1>
          <p className="auth-subtitle">
            Enter your email to receive reset instructions
          </p>
        </header>

        {!submitted ? (
          <form className="auth-form" onSubmit={handleSubmit}>
            <div className="input-group">
              <label>Email Address</label>
              <input
                type="email"
                placeholder="name@company.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>

            <button
              type="submit"
              className="btn-primary"
              disabled={loading}
            >
              {loading ? "Processing..." : "Send Recovery Link"}
            </button>
          </form>
        ) : (
          <div className="success-message">
            <p>
              If this email exists in our system, a recovery link has been sent.
            </p>
          </div>
        )}

        <footer className="auth-footer">
          <Link to="/login" className="auth-link">
            Return to <span className="highlight">Login</span>
          </Link>
        </footer>
      </div>

      <div className="terminal-info">
        <span>SECURITY PROTOCOL: RECOVERY</span>
        <span className="blink">_</span>
      </div>
    </div>
  );
};

export default ForgotPassword;
