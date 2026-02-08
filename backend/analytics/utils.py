import pandas as pd

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime


REQUIRED_COLUMNS = [
    "Equipment Name",
    "Type",
    "Flowrate",
    "Pressure",
    "Temperature"
]


def analyze_csv(file):
    df = pd.read_csv(file)

    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    summary = {
        "total_records": int(len(df)),
        "average_flowrate": float(df["Flowrate"].mean()),
        "average_pressure": float(df["Pressure"].mean()),
        "average_temperature": float(df["Temperature"].mean()),
        "type_distribution": df["Type"].value_counts().to_dict()
    }

    return summary, len(df)


def generate_pdf_report(dataset_name, summary):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 50

    # Title
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, "Chemical Equipment Parameter Analysis Report")

    y -= 30
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, y, f"Dataset: {dataset_name}")
    y -= 15
    pdf.drawString(
        50,
        y,
        f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    y -= 30
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Summary Statistics")

    y -= 20
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, y, f"Total Records: {summary['total_records']}")
    y -= 15
    pdf.drawString(
        50,
        y,
        f"Average Flowrate: {summary['average_flowrate']:.2f}"
    )
    y -= 15
    pdf.drawString(
        50,
        y,
        f"Average Pressure: {summary['average_pressure']:.2f}"
    )
    y -= 15
    pdf.drawString(
        50,
        y,
        f"Average Temperature: {summary['average_temperature']:.2f}"
    )

    y -= 30
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Equipment Type Distribution")

    y -= 20
    pdf.setFont("Helvetica", 10)
    for eq_type, count in summary["type_distribution"].items():
        pdf.drawString(50, y, f"{eq_type}: {count}")
        y -= 15

    y -= 20
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Conclusion")

    y -= 20
    pdf.setFont("Helvetica", 10)
    pdf.drawString(
        50,
        y,
        "The dataset provides a clear overview of operational parameters "
        "and equipment distribution, supporting further engineering analysis."
    )

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return buffer
