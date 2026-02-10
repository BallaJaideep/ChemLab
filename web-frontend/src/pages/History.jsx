// import { useEffect, useState } from "react";
// import { fetchHistory, downloadPDF } from "../services/api";
// import { useNavigate } from "react-router-dom";

// const History = () => {
//   const [history, setHistory] = useState([]);
//   const navigate = useNavigate();

//   useEffect(() => {
//     fetchHistory().then(setHistory);
//   }, []);

//   return (
//     <div className="page">
//       <h2 className="page-title">Recent Uploads</h2>

//       <div className="table-container">
//         <table className="data-table">
//           <thead>
//             <tr>
//               <th>#</th>
//               <th>Dataset Name</th>
//               <th>Uploaded At</th>
//               <th>Actions</th>
//             </tr>
//           </thead>

//           <tbody>
//             {history.length === 0 && (
//               <tr>
//                 <td colSpan="4" style={{ textAlign: "center" }}>
//                   No uploads yet
//                 </td>
//               </tr>
//             )}

//             {history.map((item, index) => (
//               <tr key={item.id}>
//                 <td>{index + 1}</td>
//                 <td>{item.filename}</td>
//                 <td>
//                   {new Date(item.uploaded_at).toLocaleString()}
//                 </td>
//                 <td className="action-buttons">
//                   <button
//                     className="btn btn-primary"
//                     onClick={() => navigate(`/dataset/${item.id}`)}
//                   >
//                     View Data
//                   </button>

//                   <button
//                     className="btn btn-secondary"
//                     onClick={() =>
//                       downloadPDF(item.id, item.filename)
//                     }
//                   >
//                     Download PDF
//                   </button>
//                 </td>
//               </tr>
//             ))}
//           </tbody>
//         </table>
//       </div>
//     </div>
//   );
// };

// export default History;

import { useEffect, useState } from "react";
import { fetchHistory, downloadPDF } from "../services/api";
import { useNavigate } from "react-router-dom";
import "../styles/history.css";

const History = () => {
  const [history, setHistory] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetchHistory().then(setHistory);
  }, []);

  return (
    <div className="archive-root">
      <header className="archive-header">
        <h2 className="archive-title">Dataset History Repository</h2>
        <p className="archive-subtitle">
          Review and manage historical chemical datasets stored within the secure cloud environment.
        </p>
      </header>

      <div className="archive-container">
        <table className="archive-table">
          <thead>
            <tr>
              <th className="cell-id">#</th>
              <th>Dataset Name</th>
              <th>Uploaded Timestamp</th>
              <th>Status</th>
              <th className="cell-actions">Execution Actions</th>
            </tr>
          </thead>

          <tbody>
            {history.length === 0 ? (
              <tr>
                <td colSpan="5" className="empty-state">
                  <div className="empty-msg">
                    <span className="empty-icon">📂</span>
                    No records found in the current archive.
                  </div>
                </td>
              </tr>
            ) : (
              history.map((item, index) => (
                <tr key={item.id} className="archive-row">
                  <td className="cell-id">{(index + 1).toString().padStart(2, '0')}</td>
                  <td className="cell-filename">
                    <div className="file-box">
                      <span className="file-icon">📁</span>
                      <span className="filename-text">{item.filename}</span>
                    </div>
                  </td>
                  <td className="cell-date">
                    {new Date(item.uploaded_at).toLocaleString('en-GB', {
                      day: '2-digit',
                      month: 'short',
                      year: 'numeric',
                      hour: '2-digit',
                      minute: '2-digit'
                    })}
                  </td>
                  <td className="cell-status">
                    <span className="status-pill">Verified</span>
                  </td>
                  <td className="cell-actions">
                    <div className="action-group">
                      <button
                        className="btn-action btn-view"
                        title="View Dataset"
                        onClick={() => navigate(`/dataset/${item.id}`)}
                      >
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
                        Inspect
                      </button>

                      <button
                        className="btn-action btn-download"
                        title="Download PDF Report"
                        onClick={() => downloadPDF(item.id, item.filename)}
                      >
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
                        Export
                      </button>
                    </div>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default History;