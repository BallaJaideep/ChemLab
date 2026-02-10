import { useNavigate } from "react-router-dom";
import "../styles/home.css";

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="home-root">
   
      <section className="hero-wrap">
        <h1 className="hero-main-title">Chem<span className="accent">Lab</span></h1>
        <p className="hero-tagline">
          The ultimate professional environment for chemical data processing. 
          Upload, analyze, and visualize with laboratory precision.
        </p>
      </section>

      <section className="upload-container">
        <div className="upload-box" onClick={() => navigate("/upload")}>
          <div className="upload-info">
            <div className="icon-wrapper-main">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M17 8l-5-5-5 5M12 3v12"/></svg>
            </div>
            <div className="text-stack">
              <h3>Start New Analysis</h3>
              <p>Initialize your CSV dataset for automated processing</p>
            </div>
          </div>
          <button className="upload-action-btn">Upload Dataset</button>
        </div>
      </section>

      <section className="feature-grid">
        
    
        <div className="action-card purple-theme" onClick={() => navigate("/upload")}>
          <div className="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
          </div>
          <div className="card-meta">
            <h3>Inventory View</h3>
            <p>Verify detailed equipment summaries and distribution records.</p>
          </div>
        </div>

  
        <div className="action-card cobalt-theme" onClick={() => navigate("/analysis")}>
          <div className="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          </div>
          <div className="card-meta">
            <h3>Metric Analysis</h3>
            <p>Compute automated summary statistics and equipment averages.</p>
          </div>
        </div>

  
        <div className="action-card emerald-theme" onClick={() => navigate("/charts")}>
          <div className="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
          </div>
          <div className="card-meta">
            <h3>Visual Analytics</h3>
            <p>Render high-fidelity graphical data for technical interpretation.</p>
          </div>
        </div>

      
        <div className="action-card amber-theme" onClick={() => navigate("/history")}>
          <div className="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/></svg>
          </div>
          <div className="card-meta">
            <h3>Report Archive</h3>
            <p>Access historical analytics and export professional PDF documents.</p>
          </div>
        </div>

      </section>

      
      <footer className="home-footer">
        <div className="footer-wrap">
          <div className="footer-brand">⬢ ChemLab Analytics</div>
          <div className="footer-contact">
            <span>Developer: Jaideep</span>
            <span className="divider">|</span>
            <a href="mailto:ballajaideep@gmail.com">ballajaideep@gmail.com</a>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Home;
