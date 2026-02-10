import { NavLink, useNavigate } from "react-router-dom";
import { isAuthenticated, removeToken } from "../services/auth";
import "../styles/Navbar.css";

const Navbar = () => {
  const navigate = useNavigate();
  const loggedIn = isAuthenticated();

  const handleLogout = () => {
    removeToken();
    navigate("/login");
  };

  return (
    <nav className="navbar">
      <div className="nav-container">
        {/* Professional Crossed Flasks Logo */}
        <div className="navbar-brand">
          <div className="brand-logo-wrapper">
            <svg 
              width="32" 
              height="32" 
              viewBox="0 0 24 24" 
              fill="none" 
              className="flask-svg"
            >
              {/* Flask 1 - Angled Right */}
              <path 
                d="M9.5 3L11 9L6 19C5.5 20 6.2 21 7.3 21H16.7C17.8 21 18.5 20 18 19L13 9L14.5 3" 
                stroke="#2563eb" 
                strokeWidth="1.5" 
                strokeLinecap="round"
              />
              {/* Test Tube 2 - Crossed Left */}
              <rect 
                x="4" y="8" width="4" height="14" rx="2" 
                transform="rotate(-45 4 8)" 
                stroke="#1e293b" 
                strokeWidth="1.5"
              />
              {/* Falling Liquid Drop Detail */}
              <circle cx="12" cy="14" r="1" fill="#2563eb" className="liquid-drop" />
            </svg>
          </div>
          <span className="brand-text">Chem<span className="text-bold">Lab</span></span>
        </div>

        <div className="navbar-links">
          {loggedIn ? (
            <div className="nav-menu">
              <NavLink to="/" className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}>Home</NavLink>
              <NavLink to="/upload" className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}>Upload</NavLink>
              <NavLink to="/history" className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}>History</NavLink>
              <NavLink to="/analysis" className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}>Analysis</NavLink>
              <NavLink to="/charts" className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}>Charts</NavLink>
              
              <button onClick={handleLogout} className="logout-btn">
                Logout
              </button>
            </div>
          ) : (
            <div className="nav-menu">
              <NavLink to="/login" className="nav-link">Login</NavLink>
              <NavLink to="/register" className="nav-link register-highlight">Register</NavLink>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;