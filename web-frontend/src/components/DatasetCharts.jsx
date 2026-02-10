import { Bar, Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend
);

const DatasetCharts = ({ summary }) => {
  const labels = Object.keys(summary.type_distribution);
  const values = Object.values(summary.type_distribution);

  const barData = {
    labels,
    datasets: [
      {
        label: "Equipment Count",
        data: values,
        backgroundColor: "#1f3a5f",
      },
    ],
  };

  const pieData = {
    labels,
    datasets: [
      {
        data: values,
        backgroundColor: [
          "#1f3a5f",
          "#3b82f6",
          "#64748b",
          "#94a3b8",
          "#cbd5e1",
          "#0f172a",
        ],
      },
    ],
  };

  return (
    <div className="charts-grid">
      <div className="chart-card">
        <Bar data={barData} />
      </div>

      <div className="chart-card">
        <Pie data={pieData} />
      </div>
    </div>
  );
};

export default DatasetCharts;
