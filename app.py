import os
import sqlite3

from flask import Flask, render_template_string, request

from src.build import build_html
from src.clean import clean_text
from src.convert import pdf_to_html
from src.extract import extract_pdf

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Vulnerable Endpoint 1: Directory Traversal
@app.route("/download")
def download():
    # Get filename directly from query parameter (vulnerable to directory traversal)
    filename = request.args.get("file")
    # Intentionally no sanitization
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(file_path, "r") as f:
        content = f.read()
    return content


# Vulnerable Endpoint 2: SQL Injection & XSS Issue
@app.route("/log", methods=["GET", "POST"])
def log():
    conn = sqlite3.connect("logs.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, message TEXT)")
    if request.method == "POST":
        user_message = request.form.get("message")
        # Vulnerability: unsanitized SQL query construction allows SQL injection
        query = "INSERT INTO logs (message) VALUES ('{}')".format(user_message)
        c.execute(query)
        conn.commit()
        conn.close()
        return "Logged!"
    else:
        # Vulnerability: unsanitized display leads to XSS in the browser if user_message includes scripts
        c.execute("SELECT message FROM logs")
        messages = c.fetchall()
        output = "<h1>Logs</h1>"
        for msg in messages:
            output += "<p>" + msg[0] + "</p>"
        conn.close()
        return output


# Endpoint for file upload and conversion integration
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # Vulnerability: file upload is not sanitized (no secure_filename)
        file = request.files["pdf"]
        filename = file.filename  # intentionally vulnerable
        upload_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(upload_path)

        # Call conversion functions from your project.
        page_number = 0  # For simplicity (could be extended)
        text_attributes_list = extract_pdf(upload_path, page_number)
        text_attributes_list = clean_text(text_attributes_list)
        html_list = pdf_to_html(text_attributes_list)
        output_file = os.path.join(UPLOAD_FOLDER, filename + ".html")
        build_html(html_list, output_file, page_number)

        return render_template_string(
            """
            <h1>Conversion Result</h1>
            <iframe src="/view?file={{ file }}" width="800" height="600"></iframe>
        """,
            file=filename + ".html",
        )
    return """
    <h1>Upload PDF</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="pdf">
      <input type="submit" value="Upload">
    </form>
    """


# Endpoint to display converted HTML content
@app.route("/view")
def view():
    file = request.args.get("file")
    file_path = os.path.join(UPLOAD_FOLDER, file)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content


if __name__ == "__main__":
    app.run(debug=True)
