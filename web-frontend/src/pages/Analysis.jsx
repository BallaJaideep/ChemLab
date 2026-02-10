import { useEffect, useState } from "react";
import { fetchHistory, fetchDatasetDetail } from "../services/api";
import "../styles/analysis.css";

const Analysis = () => {
  const [dataset, setDataset] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchHistory().then((h) => {
      if (h.length > 0) {
        fetchDatasetDetail(h[0].id).then((data) => {
          setDataset(data);
          setLoading(false);
        });
      } else {
        setLoading(false);
      }
    });
  }, []);

  if (loading) return (
    <div className="analysis-loading">
      <div className="analysis-spinner"></div>
      <p>Retrieving latest telemetry data...</p>
    </div>
  );

  if (!dataset) return (
    <div className="analysis-empty">
      <p>No processed datasets found. Please upload a CSV to begin analysis.</p>
    </div>
  );

  const { filename, summary } = dataset;

  return (
    <div className="analysis-root">
      <header className="analysis-header">
        <div className="analysis-title-group">
          <span className="live-badge">Live Analysis</span>
          <h2 className="analysis-main-title">Latest Summary Statistics</h2>
          <p className="analysis-file-ref">Active Dataset: <strong>{filename}</strong></p>
        </div>
      </header>

      {/* Primary Metrics Grid */}
      <section className="analysis-stats-grid">
        <div className="stat-card">
          <div className="stat-label">Total Records Verified</div>
          <div className="stat-value">{summary.total_records}</div>
          <div className="stat-footer">Nodes Processed</div>
        </div>

        <div className="stat-card accent-blue">
          <div className="stat-label">Avg Flowrate</div>
          <div className="stat-value">{summary.average_flowrate.toFixed(2)}</div>
          <div className="stat-footer">Cubic Meters / Hour</div>
        </div>

        <div className="stat-card accent-teal">
          <div className="stat-label">Avg Pressure</div>
          <div className="stat-value">{summary.average_pressure.toFixed(2)}</div>
          <div className="stat-footer">Barometric Pressure</div>
        </div>

        <div className="stat-card accent-purple">
          <div className="stat-label">Avg Temperature</div>
          <div className="stat-value">{summary.average_temperature.toFixed(2)}</div>
          <div className="stat-footer">Degrees Celsius</div>
        </div>
      </section>

      {/* Distribution Section */}
      <section className="analysis-distribution">
        <div className="distribution-card">
          <div className="dist-header">
            <h3>Equipment Categorical Breakdown</h3>
            <span className="dist-tag">Unit Distribution</span>
          </div>
          <div className="dist-list">
            {Object.entries(summary.type_distribution).map(([type, count]) => (
              <div key={type} className="dist-item">
                <div className="dist-type-name">{type}</div>
                <div className="dist-progress-container">
                  <div 
                    className="dist-progress-bar" 
                    style={{ width: `${(count / summary.total_records) * 100}%` }}
                  ></div>
                </div>
                <div className="dist-count"><strong>{count}</strong> Units</div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
};

export default Analysis;