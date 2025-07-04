from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import os
from .audio_utils import analyze_and_normalize
from .pdf_report import create_pdf_report

app = FastAPI()

UPLOAD_DIR = "uploads"
NORMALIZED_DIR = "normalized"
REPORT_DIR = "reports"

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("app/templates/index.html") as f:
        return f.read()

@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    try:
        filename = file.filename
        filepath = os.path.join(UPLOAD_DIR, filename)

        # Ensure upload directory exists
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        # Save file
        with open(filepath, "wb") as f:
            f.write(await file.read())

        # Process file
        lufs_before, lufs_after, peak, normalized_path = analyze_and_normalize(filepath)

        # Create report
        pdf_path = create_pdf_report(filename, lufs_before, lufs_after, peak)

        return {
            "message": "File processed successfully",
            "lufs_before": lufs_before,
            "lufs_after": lufs_after,
            "peak": peak,
            "normalized_audio": f"/normalized/{os.path.basename(normalized_path)}",
            "report": f"/reports/{os.path.basename(pdf_path)}"
        }

    except Exception as e:
        print(f"🔥 ERROR: {str(e)}")  # Show in terminal
        return {"error": str(e)}  # Show in browser
