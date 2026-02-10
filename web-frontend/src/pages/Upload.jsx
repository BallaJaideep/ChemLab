import { useState } from "react";
import { uploadDataset } from "../services/api";
import "../styles/upload.css";

const Upload = () => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState(null);

  const handleUpload = async () => {
    if (!file) {
      setError("Selection Required: Please provide a valid CSV file.");
      return;
    }

    setError("");
    setSuccess(null);
    setLoading(true);

    try {
      const data = await uploadDataset(file);
      setSuccess({
        filename: file.name,
        records: data.summary.total_records,
      });
    } catch (err) {
      setError(err?.response?.data?.error || "Ingestion Error: Check CSV schema.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="ingestion-root">
      <div className="ingestion-bg-decor"></div>
      
      <div className="ingestion-container">
        <header className="ingestion-header">
          <h1 className="ingestion-title">Data Ingestion Terminal</h1>
          <p className="ingestion-subtitle">
            Upload equipment telemetry logs for automated parametric validation.
          </p>
        </header>

        <div className="ingestion-card">
          {/* Instructions Box */}
          <div className="ingestion-checklist">
            <h4>Dataset Requirements:</h4>
            <ul>
              <li>File format must be strictly <strong>.CSV</strong></li>
              <li>Required columns: <code>Equipment_Name</code>, <code>Parameter_Value</code></li>
              <li>Maximum file size: 10MB</li>
            </ul>
          </div>

          {/* Professional Dropzone Area */}
          <div className={`dropzone-area ${file ? "file-selected" : ""}`}>
            <input
              type="file"
              accept=".csv"
              id="csv-upload"
              className="hidden-input"
              onChange={(e) => {
                setFile(e.target.files[0]);
                setError("");
              }}
            />
            <label htmlFor="csv-upload" className="dropzone-label">
              <div className="dropzone-icon">
                {file ? "📄" : "📤"}
              </div>
              <div className="dropzone-text">
                {file ? (
                  <span className="filename-display">{file.name}</span>
                ) : (
                  <>
                    <strong>Click to select</strong> or drag and drop
                    <small>Only CSV files are accepted</small>
                  </>
                )}
              </div>
            </label>
          </div>

          <button
            className={`process-btn ${loading ? "btn-loading" : ""}`}
            onClick={handleUpload}
            disabled={loading}
          >
            {loading ? (
              <span className="loader-flex">
                <span className="spinner"></span> Processing...
              </span>
            ) : (
              "Analyze & Upload"
            )}
          </button>

          {/* Status Feedback Messaging */}
          {error && (
            <div className="feedback-msg error-msg">
              <span className="msg-icon">⚠️</span> {error}
            </div>
          )}

          {success && (
            <div className="feedback-msg success-msg">
              <div className="success-header">
                <span className="msg-icon">✓</span> <strong>Ingestion Successful</strong>
              </div>
              <div className="success-details">
                <p>Node: {success.filename}</p>
                <p>Records Verified: {success.records}</p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Upload;