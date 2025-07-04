from fpdf import FPDF
import os

def create_pdf_report(filename, lufs_before, lufs_after, peak):
    report_path = os.path.join("reports", f"{filename}.pdf")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="LUFS Normalization Report", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Filename: {filename}", ln=True)
    pdf.cell(200, 10, txt=f"LUFS Before: {lufs_before}", ln=True)
    pdf.cell(200, 10, txt=f"LUFS After: {lufs_after}", ln=True)
    pdf.cell(200, 10, txt=f"True Peak: {peak}", ln=True)
    pdf.output(report_path)
    return report_path
