import subprocess
import os

def analyze_and_normalize(filepath):
    # Get LUFS and Peak from FFmpeg loudnorm
    cmd = [
        "ffmpeg", "-i", filepath,
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=summary",
        "-f", "null", "-"
    ]
    result = subprocess.run(cmd, stderr=subprocess.PIPE, text=True)
    output = result.stderr

    # Parse LUFS and Peak
    lufs_before = extract_value(output, "Input Integrated")
    peak = extract_value(output, "Input True Peak")

    # Normalize audio
    output_path = os.path.join("normalized", os.path.basename(filepath))
    norm_cmd = [
        "ffmpeg", "-i", filepath,
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", output_path
    ]
    subprocess.run(norm_cmd)

    return lufs_before, "-14", peak, output_path

def extract_value(text, key):
    for line in text.splitlines():
        if key in line:
            return line.split(":")[-1].strip()
    return "N/A"
