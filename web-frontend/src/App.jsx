import { Routes, Route, Navigate } from "react-router-dom";

/* ===== PUBLIC PAGES ===== */
import Login from "./pages/Login";
import Register from "./pages/Register";
import ForgotPassword from "./pages/ForgotPassword";
import ResetPassword from "./pages/ResetPassword";

/* ===== PROTECTED PAGES ===== */
import Home from "./pages/Home";
import Upload from "./pages/Upload";
import History from "./pages/History";
import DatasetView from "./pages/DatasetView";
import Analysis from "./pages/Analysis";
import Charts from "./pages/Charts";

/* ===== LAYOUT & AUTH ===== */
import ProtectedRoute from "./components/ProtectedRoute";
import MainLayout from "./layout/MainLayout";

const App = () => {
  return (
    <Routes>
      {/* ================= PUBLIC ROUTES ================= */}
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/forgot-password" element={<ForgotPassword />} />
      <Route
        path="/reset-password/:uid/:token"
        element={<ResetPassword />}
      />

      {/* ================= PROTECTED ROUTES ================= */}
      <Route
        path="/"
        element={
          <ProtectedRoute>
            <MainLayout>
              <Home />
            </MainLayout>
          </ProtectedRoute>
        }
      />

      <Route
        path="/upload"
        element={
          <ProtectedRoute>
            <MainLayout>
              <Upload />
            </MainLayout>
          </ProtectedRoute>
        }
      />

      <Route
        path="/history"
        element={
          <ProtectedRoute>
            <MainLayout>
              <History />
            </MainLayout>
          </ProtectedRoute>
        }
      />

      <Route
        path="/dataset/:id"
        element={
          <ProtectedRoute>
            <MainLayout>
              <DatasetView />
            </MainLayout>
          </ProtectedRoute>
        }
      />

      <Route
        path="/analysis"
        element={
          <ProtectedRoute>
            <MainLayout>
              <Analysis />
            </MainLayout>
          </ProtectedRoute>
        }
      />

      <Route
        path="/charts"
        element={
          <ProtectedRoute>
            <MainLayout>
              <Charts />
            </MainLayout>
          </ProtectedRoute>
        }
      />

      {/* ================= FALLBACK ROUTE ================= */}
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
  );
};

export default App;
