from reportlab.lib.pagesizes import letter  # import letter size page
from reportlab.pdfgen import canvas  # used for writing on the page
from db import fetch_predictions

def generate_report(pdf_path='exam_report.pdf'):
    preds = fetch_predictions()
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height-50, "Smart Exam Performance Analyzer Report")

    c.setFont("Helvetica", 12)
    y = height - 80
    c.drawString(50, y, "Predictions:")
    y -= 20

    for sid, name, pred, reason, when in preds:
        line = f"{when.strftime('%Y-%m-%d %H:%M')} — {name} (ID {sid}): {pred} | {reason}"
        c.drawString(60, y, line)
        y -= 15
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    return pdf_path
