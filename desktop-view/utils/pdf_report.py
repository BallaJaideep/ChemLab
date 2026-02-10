# utils/pdf_report.py

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime


def generate_pdf_report(filename, summary, output_path):
    """
    Generates a professional PDF report for a dataset
    """

    pdf = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    x_margin = 50
    y = height - 50

    # ================= TITLE =================
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(
        x_margin,
        y,
        "Chemical Equipment Analysis Report"
    )

    y -= 30
    pdf.setFont("Helvetica", 10)
    pdf.drawString(
        x_margin,
        y,
        f"Dataset: {filename}"
    )
    pdf.drawRightString(
        width - x_margin,
        y,
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    # ================= SUMMARY =================
    y -= 40
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(x_margin, y, "Summary Statistics")

    y -= 20
    pdf.setFont("Helvetica", 11)

    pdf.drawString(
        x_margin,
        y,
        f"Total Records: {summary.get('total_records', 0)}"
    )

    y -= 18
    pdf.drawString(
        x_margin,
        y,
        f"Average Flowrate: {summary.get('average_flowrate', 0):.2f}"
    )

    y -= 18
    pdf.drawString(
        x_margin,
        y,
        f"Average Pressure: {summary.get('average_pressure', 0):.2f}"
    )

    y -= 18
    pdf.drawString(
        x_margin,
        y,
        f"Average Temperature: {summary.get('average_temperature', 0):.2f}"
    )

    # ================= DISTRIBUTION =================
    y -= 35
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(
        x_margin,
        y,
        "Equipment Type Distribution"
    )

    y -= 20
    pdf.setFont("Helvetica", 11)

    distribution = summary.get("type_distribution", {})

    if not distribution:
        pdf.drawString(x_margin, y, "No distribution data available.")
    else:
        for eq_type, count in distribution.items():
            if y < 80:
                pdf.showPage()
                pdf.setFont("Helvetica", 11)
                y = height - 50

            pdf.drawString(
                x_margin,
                y,
                f"{eq_type}: {count}"
            )
            y -= 16

    # ================= FOOTER =================
    pdf.showPage()
    pdf.save()
