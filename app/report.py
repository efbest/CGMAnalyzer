from fpdf import FPDF
from datetime import datetime

def generate_pdf_report(df, metrics, source, filepath):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "CGM Clinical Insights Report", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Prepared by: Frank Best", ln=True)
    pdf.cell(0, 10, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
    pdf.cell(0, 10, f"Source Device: {source}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Glucose Metrics:", ln=True)

    pdf.set_font("Arial", "", 12)
    for k, v in metrics.items():
        pdf.cell(0, 8, f"{k}: {v}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "I", 10)
    pdf.multi_cell(0, 8, "This report was generated using CGMAnalyzer with dolphin branding for clinical use.")

    pdf.output(filepath)
