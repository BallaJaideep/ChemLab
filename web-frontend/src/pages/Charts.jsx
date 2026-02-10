import { useEffect, useState } from "react";
import { fetchHistory, fetchDatasetDetail } from "../services/api";
import { Bar } from "react-chartjs-2";
import "../styles/charts.css";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Filler,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend,
  Filler
);

const Charts = () => {
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadChartData = async () => {
      try {
        const history = await fetchHistory();
        if (history.length === 0) {
          setLoading(false);
          return;
        }
        const dataset = await fetchDatasetDetail(history[0].id);
        setSummary(dataset.summary);
      } catch (error) {
        console.error("Failed to load chart data", error);
      } finally {
        setLoading(false);
      }
    };
    loadChartData();
  }, []);

  if (loading) return (
    <div className="charts-loader">
      <div className="spinner"></div>
      <p>Rendering Visual Telemetry...</p>
    </div>
  );

  if (!summary) return (
    <div className="charts-empty">
      <p>No processed datasets found in the repository.</p>
    </div>
  );

  const chartData = {
    labels: Object.keys(summary.type_distribution),
    datasets: [
      {
        label: "Unit Count",
        data: Object.values(summary.type_distribution),
        backgroundColor: "rgba(37, 99, 235, 0.8)",
        hoverBackgroundColor: "#1d4ed8",
        borderRadius: 6,
        borderWidth: 0,
        barThickness: 'flex',
        maxBarThickness: 40,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false,
      },
      tooltip: {
        backgroundColor: "#0f172a",
        padding: 12,
        titleFont: { size: 14, weight: 'bold' },
        bodyFont: { size: 13 },
        cornerRadius: 8,
        displayColors: false
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        grid: { color: "#f1f5f9", drawBorder: false },
        ticks: { color: "#64748b", font: { size: 12 } }
      },
      x: {
        grid: { display: false },
        ticks: { color: "#64748b", font: { size: 12, weight: '600' } }
      }
    }
  };

  return (
    <div className="charts-root">
      <header className="charts-header">
        <div className="header-meta">
          <span className="node-tag">Visualization_Engine</span>
          <h1 className="charts-title">Graphical Distribution</h1>
          <p className="charts-subtitle">
            Visual breakdown of equipment categories for the most recent analytical cycle.
          </p>
        </div>
      </header>

      <div className="charts-main-layout">
        <div className="chart-card-full">
          <div className="card-top-row">
            <h3>Categorical Telemetry</h3>
            <div className="chart-legend">
              <span className="legend-dot"></span> Equipment Type Distribution
            </div>
          </div>
          <div className="chart-render-area">
            <Bar data={chartData} options={chartOptions} />
          </div>
        </div>

        <aside className="chart-sidebar">
          <div className="insight-card">
            <h4>Technical Summary</h4>
            <div className="insight-stat">
              <label>Unique Categories</label>
              <strong>{Object.keys(summary.type_distribution).length}</strong>
            </div>
            <div className="insight-stat">
              <label>Total Units Mapped</label>
              <strong>{summary.total_records}</strong>
            </div>
          </div>
          <div className="hint-card">
            <p>Hover over the bars to view precise equipment counts for each chemical node.</p>
          </div>
        </aside>
      </div>
    </div>
  );
};

export default Charts;

