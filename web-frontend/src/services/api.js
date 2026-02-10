import axios from "axios";
import { getToken } from "./auth";

/* ================= BASE API INSTANCE ================= */

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
  headers: {
    "Content-Type": "application/json",
  },
});

/* ================= JWT INTERCEPTOR ================= */

api.interceptors.request.use(
  (config) => {
    const token = getToken();

    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
  },
  (error) => Promise.reject(error)
);

/* ================= AUTH ================= */

/* ✅ LOGIN */
export const loginUser = async (credentials) => {
  const res = await api.post("auth/login/", credentials);
  return res.data;
};

/* ✅ REGISTER */
export const registerUser = async (data) => {
  const res = await api.post("auth/register/", data);
  return res.data;
};

/* ================= DATA UPLOAD ================= */

export const uploadDataset = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const res = await api.post("upload/", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return res.data;
};

/* ================= HISTORY ================= */

export const fetchHistory = async () => {
  const res = await api.get("history/");
  return res.data;
};

/* ================= DATASET DETAIL ================= */

export const fetchDatasetDetail = async (id) => {
  const res = await api.get(`dataset/${id}/`);
  return res.data;
};

/* ================= PDF DOWNLOAD ================= */

export const downloadPDF = async (id, filename) => {
  const res = await api.get(`dataset/${id}/pdf/`, {
    responseType: "blob",
  });

  const blob = new Blob([res.data], { type: "application/pdf" });
  const url = window.URL.createObjectURL(blob);

  const link = document.createElement("a");
  link.href = url;
  link.download = `${filename}_report.pdf`;

  document.body.appendChild(link);
  link.click();

  link.remove();
  window.URL.revokeObjectURL(url);
};

/* ================= EXPORT DEFAULT ================= */

export default api;
