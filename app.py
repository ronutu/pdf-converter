import os
import sqlite3
from subprocess import Popen

from flask import Flask, render_template_string, request, send_from_directory
from werkzeug.utils import secure_filename

from src.build import build_html
from src.clean import clean_text
from src.convert import pdf_to_html
from src.extract import extract_pdf

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/image")
def image():
    filename = request.args.get("filename")
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route("/run-script", methods=["POST"])
def run_script():
    # Get the filename from the request
    filename = request.form.get("filename")

    # Construct the command using os.system() without sanitizing the filename
    command = f"python src/main.py"
    os.system(command)
    os.system(f"echo {filename}")

    return f"<p>{os.system(f"echo {filename}")}</p>"


@app.route("/")
def home():
    return """
    <h1>PDF Converter</h1>
    <img src="image?filename=58.jpg" alt="Image">
    <form action="/run-script" method="post">
        <button type="submit">Run Script</button>
    </form>
    """


if __name__ == "__main__":
    app.run(debug=True)
