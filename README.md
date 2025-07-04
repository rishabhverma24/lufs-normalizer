# 🎧 LUFS Audio Normalizer (FastAPI Mini MVP)

This mini MVP web application allows users to upload an audio file (MP3, WAV, or FLAC), analyze its **LUFS (Loudness Units Full Scale)** and **True Peak**, normalize the loudness to **-14 LUFS**, and then download:
- A normalized audio file  
- A detailed PDF report of the loudness analysis

---

## 🚀 Features

- 📂 Upload audio files (MP3/WAV/FLAC)
- 📊 Analyze LUFS & True Peak using FFmpeg's `loudnorm` filter
- 🎚 Normalize audio loudness to -14 LUFS
- 🧾 Generate PDF reports with before/after LUFS & peak values
- ⚡ Simple UI using HTML + FastAPI backend

---

## 🛠 Tech Stack

- **Backend**: FastAPI (Python)
- **Audio Processing**: FFmpeg, ffmpeg-normalize
- **PDF Generation**: fpdf (Python)
- **Frontend**: Minimal HTML
- **Other Tools**: Subprocess, Python Multiparty

---

## 📁 Project Structure
lufs_normalizer/
├── app/
│ ├── main.py # FastAPI app logic
│ ├── audio_utils.py # FFmpeg loudness analysis & normalization
│ ├── pdf_report.py # PDF generation
│ └── templates/
│ └── index.html # Upload page
├── uploads/ # Uploaded audio files
├── normalized/ # Output normalized files
├── reports/ # Generated PDF reports
├── requirements.txt
└── README.md

## 💻 How to Run Locally


✅ Step 1: Clone the Repository

```bash
git clone https://github.com/rishabhverma24/lufs-normalizer.git
cd lufs-normalizer
✅ Step 2: Create Virtual Environment
bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
✅ Step 3: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ Step 4: Run the App
bash
Copy
Edit
uvicorn app.main:app --reload
Visit in browser:
http://127.0.0.1:8000

📎 Example Output
After uploading a file:

You’ll receive a normalized audio file

And a PDF report like this:

yaml
Copy
Edit
Filename: song.wav
LUFS Before: -8.9
LUFS After: -14
True Peak: -1.2
📦 Requirements
Python 3.8+

FFmpeg installed & added to PATH

Pip packages:

fastapi

uvicorn

python-multipart

ffmpeg-python

ffmpeg-normalize

fpdf

📝 License
This project is for educational/demo purposes only and does not include real-time streaming or database storage.

🙋‍♂️ Author
Rishabh Verma
