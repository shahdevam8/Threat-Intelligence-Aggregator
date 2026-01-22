import csv
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

REPORT_DIR = "reports"

def generate_csv_report(iocs):
    csv_file = os.path.join(REPORT_DIR, "TI_Report.csv")
    with open(csv_file, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["value","type","source","severity","timestamp"])
        writer.writeheader()
        writer.writerows(iocs)

def generate_pdf_report(iocs):
    pdf_file = os.path.join(REPORT_DIR, "TI_Report.pdf")
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.setFont("Helvetica", 12)
    y = 750
    c.drawString(50, y, "Threat Intelligence Aggregator Report")
    y -= 30
    for ioc in iocs:
        line = f"{ioc['value']} | {ioc['type']} | {ioc['severity']} | {ioc['source']} | {ioc['timestamp']}"
        c.drawString(50, y, line)
        y -= 20
        if y < 50:
            c.showPage()
            y = 750
    c.save()
