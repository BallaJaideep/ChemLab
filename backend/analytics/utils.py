import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime

# ================= REQUIRED CSV COLUMNS =================

REQUIRED_COLUMNS = [
    "Equipment Name",
    "Type",
    "Flowrate",
    "Pressure",
    "Temperature",
]

# ================= CSV ANALYSIS =================

def analyze_csv(file):
    """
    Reads CSV file, validates columns, computes summary statistics
    and returns (summary, preview)
    """

    try:
        df = pd.read_csv(file)
    except Exception:
        raise ValueError("Invalid or unreadable CSV file")

    # Normalize column names (remove extra spaces)
    df.columns = [col.strip() for col in df.columns]

    # Validate required columns
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Convert numeric columns safely
    numeric_columns = ["Flowrate", "Pressure", "Temperature"]
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows with invalid numeric data
    df = df.dropna(subset=numeric_columns)

    if df.empty:
        raise ValueError("CSV contains no valid numeric data")

    # Build summary
    summary = {
        "total_records": int(len(df)),
        "average_flowrate": float(df["Flowrate"].mean()),
        "average_pressure": float(df["Pressure"].mean()),
        "average_temperature": float(df["Temperature"].mean()),
        "type_distribution": df["Type"].value_counts().to_dict(),
    }

    # Preview first 15 rows
    preview = df.head(15).to_dict(orient="records")

    return summary, preview


# ================= PDF GENERATION =================

def generate_pdf_report(filename, summary):
    """
    Generates a PDF report from dataset summary
    """

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4
    margin_x = 50
    y = height - 50

    # ===== TITLE =====
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(
        margin_x,
        y,
        "Chemical Equipment Analysis Report"
    )

    y -= 30
    pdf.setFont("Helvetica", 10)
    pdf.drawString(margin_x, y, f"Dataset: {filename}")
    pdf.drawRightString(
        width - margin_x,
        y,
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    )

    # ===== SUMMARY =====
    y -= 40
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(margin_x, y, "Summary Statistics")

    y -= 20
    pdf.setFont("Helvetica", 10)
    pdf.drawString(
        margin_x,
        y,
        f"Total Records: {summary.get('total_records', 0)}",
    )

    y -= 15
    pdf.drawString(
        margin_x,
        y,
        f"Average Flowrate: {summary.get('average_flowrate', 0):.2f}",
    )

    y -= 15
    pdf.drawString(
        margin_x,
        y,
        f"Average Pressure: {summary.get('average_pressure', 0):.2f}",
    )

    y -= 15
    pdf.drawString(
        margin_x,
        y,
        f"Average Temperature: {summary.get('average_temperature', 0):.2f}",
    )

    # ===== DISTRIBUTION =====
    y -= 30
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(
        margin_x,
        y,
        "Equipment Type Distribution",
    )

    y -= 20
    pdf.setFont("Helvetica", 10)

    type_distribution = summary.get("type_distribution", {})

    if not type_distribution:
        pdf.drawString(margin_x, y, "No distribution data available.")
    else:
        for eq_type, count in type_distribution.items():
            if y < 80:
                pdf.showPage()
                pdf.setFont("Helvetica", 10)
                y = height - 50

            pdf.drawString(
                margin_x,
                y,
                f"{eq_type}: {count}",
            )
            y -= 14

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return buffer

