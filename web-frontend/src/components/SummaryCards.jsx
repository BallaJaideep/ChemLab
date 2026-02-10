import "../styles/summaryCards.css";

const SummaryCards = ({ summary }) => {
  return (
    <div className="summary-grid">
      <div className="summary-card">
        <div className="label">Total Records</div>
        <div className="value">{summary.total_records}</div>
      </div>

      <div className="summary-card">
        <div className="label">Avg Flowrate</div>
        <div className="value">
          {summary.average_flowrate.toFixed(2)}
        </div>
      </div>

      <div className="summary-card">
        <div className="label">Avg Pressure</div>
        <div className="value">
          {summary.average_pressure.toFixed(2)}
        </div>
      </div>

      <div className="summary-card">
        <div className="label">Avg Temperature</div>
        <div className="value">
          {summary.average_temperature.toFixed(2)}
        </div>
      </div>
    </div>
  );
};

export default SummaryCards;
