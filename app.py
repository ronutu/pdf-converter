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

@app.route('/render')
def render_user_input():
    # Suppose the user provides some text to be displayed on the result page.
    user_content = request.args.get('content', '')
    # Directly incorporating user-supplied content into a template using render_template_string
    # Without proper sanitization, this is vulnerable to SSTI.
    template = f"<html><body><h1>User Content</h1><div>{user_content}</div></body></html>"
    return render_template_string(template)


@app.route("/logs")
def logs():
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()
    query = request.args.get("query")  # User-provided query
    result = cursor.execute(
        f"SELECT * FROM logs WHERE {query}"
    ).fetchall()  # Vulnerable to SQL Injection
    conn.close()
    return render_template_string(
        "<ul>{% for row in result %}<li>{{ row }}</li>{% endfor %}</ul>", result=result
    )


@app.route("/xss")
def xss():
    user_input = request.args.get("input")  # User-provided input
    return f"<p>{user_input}</p>"  # Rendering unsanitized input directly


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file part"
    file = request.files["file"]
    if file.filename == "":
        return "No selected file"
    # Saving the file without validating its type or content
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
    return "File uploaded successfully"


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
