# ChemLab Analytics – Full Stack Platform (Web + Desktop)

ChemLab Analytics is a **full-stack chemical data analytics platform** that includes:

- **Web Backend API**
- **Modern Web Frontend**
- **Professional Desktop Application**

All three are hosted together in **one repository** to demonstrate **real-world system architecture**, code organization, and cross-platform development.

---

## Project Purpose

Chemical laboratories and industrial plants generate large CSV datasets containing:
- Equipment Name
- Equipment Type
- Flowrate
- Pressure
- Temperature

Manual analysis is:
- Error-prone
- Time-consuming
- Hard to visualize

**ChemLab Analytics** solves this by providing:
- Structured data ingestion
- Automated statistics
- Interactive visualizations
- Dataset history tracking
- Professional PDF reporting
- Both **online (web)** and **offline (desktop)** usage

---

Each module is **independent**, but conceptually aligned.

---

## Technology Stack

### Backend (API)
- Python
- Django / FastAPI
- REST APIs
- JWT Authentication
- SQLite / PostgreSQL

### Web Frontend
- React.js
- React Router
- Modern dashboard UI
- Charts & analytics
- CSV upload

### Desktop Frontend
- Python 3
- PyQt5
- SQLite
- Pandas
- Matplotlib
- ReportLab (PDF export)
- QSS (custom styling)

---

##  Repository Structure


## Backend API (Overview)

The backend provides:
- User authentication
- Dataset management
- Analytics endpoints
- Secure API access for the web frontend

### Run Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
