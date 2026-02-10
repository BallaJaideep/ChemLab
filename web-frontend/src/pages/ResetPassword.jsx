import { useParams, useNavigate } from "react-router-dom";
import { useState } from "react";
import axios from "axios";
import "../styles/Login.css";

const ResetPassword = () => {
  const { uid, token } = useParams();
  const navigate = useNavigate();

  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const handleReset = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      await axios.post(
        `http://127.0.0.1:8000/api/auth/reset-password/${uid}/${token}/`,
        { password }
      );

      alert("Password reset successful. Please login.");
      navigate("/login");
    } catch  {
      alert("Reset link expired or invalid");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-wrapper">
      <div className="auth-card">
        <h2>Set New Password</h2>

        <form onSubmit={handleReset}>
          <input
            type="password"
            placeholder="New Password (min 8 chars)"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          <button type="submit" disabled={loading}>
            {loading ? "Resetting..." : "Reset Password"}
          </button>
        </form>
      </div>
    </div>
  );
};

export default ResetPassword;
