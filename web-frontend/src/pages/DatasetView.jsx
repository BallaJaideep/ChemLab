import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { fetchDatasetDetail } from "../services/api";
import { Bar } from "react-chartjs-2";
import "../styles/datasetView.css";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

const DatasetView = () => {
  const { id } = useParams();
  const [dataset, setDataset] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadDataset = async () => {
      try {
        const data = await fetchDatasetDetail(id);
        setDataset(data);
      } catch (err) {
        console.error("Failed to load dataset", err);
      } finally {
        setLoading(false);
      }
    };
    loadDataset();
  }, [id]);

  if (loading) return (
    <div className="dv-loader">
      <div className="spinner"></div>
      <p>Synchronizing Analytical Node...</p>
    </div>
  );

  if (!dataset) return <p className="error-text">No analytical data found for this node.</p>;

  const { filename, uploaded_at, summary, preview } = dataset;

  const chartData = {
    labels: Object.keys(summary.type_distribution),
    datasets: [
      {
        label: "Equipment Unit Count",
        data: Object.values(summary.type_distribution),
        backgroundColor: "#2563eb",
        borderRadius: 4,
        barThickness: 30,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: { legend: { display: false } },
    scales: {
      y: { beginAtZero: true, grid: { color: "#f1f5f9" } },
      x: { grid: { display: false } }
    }
  };

  return (
    <div className="dv-root">
      {/* Header Section */}
      <header className="dv-header">
        <div className="dv-header-left">
          <span className="dv-badge">Diagnostic Report</span>
          <h1 className="dv-title">{filename}</h1>
          <p className="dv-timestamp">Processed on: {new Date(uploaded_at).toLocaleString()}</p>
        </div>
        <button className="dv-export-btn" onClick={() => window.print()}>Export Brief</button>
      </header>

      {/* Metric Tiles Grid */}
      <div className="dv-metrics-grid">
        <div className="metric-tile">
          <label>Total Records</label>
          <div className="value">{summary.total_records}</div>
          <div className="unit">Data Points</div>
        </div>
        <div className="metric-tile accent-blue">
          <label>Avg Flowrate</label>
          <div className="value">{summary.average_flowrate.toFixed(2)}</div>
          <div className="unit">m³/h</div>
        </div>
        <div className="metric-tile accent-teal">
          <label>Avg Pressure</label>
          <div className="value">{summary.average_pressure.toFixed(2)}</div>
          <div className="unit">Bar</div>
        </div>
        <div className="metric-tile accent-purple">
          <label>Avg Temperature</label>
          <div className="value">{summary.average_temperature.toFixed(2)}</div>
          <div className="unit">°C</div>
        </div>
      </div>

      {/* Middle Section: Distribution & Chart */}
      <div className="dv-analysis-row">
        <div className="dv-card distribution-list">
          <h3>Equipment Distribution</h3>
          <div className="dist-items">
            {Object.entries(summary.type_distribution).map(([k, v]) => (
              <div key={k} className="dist-row">
                <span className="dist-key">{k}</span>
                <span className="dist-val">{v} units</span>
              </div>
            ))}
          </div>
        </div>

        <div className="dv-card chart-container">
          <h3>Categorical Visualization</h3>
          <div className="chart-wrapper">
            <Bar data={chartData} options={chartOptions} />
          </div>
        </div>
      </div>

      {/* Bottom Section: Data Table */}
      <div className="dv-card table-card">
        <div className="table-header">
          <h3>Telemetry Preview (Head 15)</h3>
          <span className="table-tag">Raw CSV Data</span>
        </div>
        <div className="table-scroll">
          <table className="dv-table">
            <thead>
              <tr>
                {Object.keys(preview[0]).map((col) => (
                  <th key={col}>{col}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {preview.map((row, idx) => (
                <tr key={idx}>
                  {Object.values(row).map((val, i) => (
                    <td key={i}>{typeof val === 'number' ? val.toFixed(2) : val}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default DatasetView;
