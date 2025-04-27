import os
import sqlite3
import urllib.parse
from subprocess import getoutput

from flask import Flask, render_template, render_template_string, request, send_file

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/image")
def image():
    raw_name = request.args.get("filename", "")
    if "../" in raw_name or "%2e" in raw_name.lower():
        return "❌ Suspicious filename", 400

    filename = urllib.parse.unquote(raw_name)
    file_path = os.path.join(BASE_DIR, filename)
    try:
        return send_file(file_path)
    except FileNotFoundError:
        return "❌ File not found", 404


@app.route("/run-script", methods=["POST"])
def run_script():

    filename = request.form.get("filename", "")

    os.system("python src/main.py")
    output = getoutput(f"echo {filename}")
    return f"<pre>{output}</pre>"


@app.route("/render", methods=["GET", "POST"])
def unsafe_render():
    user_content = request.values.get("content", "")
    return render_template_string(user_content)


@app.route("/logs")
def logs():
    query = request.args.get("query", "1=1")
    conn = sqlite3.connect("logs.db")
    cur = conn.cursor()
    rows = cur.execute(f"SELECT * FROM logs WHERE {query}").fetchall()
    conn.close()
    return render_template_string(
        "<ul>{% for r in rows %}<li>{{ r }}</li>{% endfor %}</ul>", rows=rows
    )


@app.route("/xss")
def xss():
    user_input = request.args.get("input", "")
    return f"<p>{user_input}</p>"


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files or request.files["file"].filename == "":
        return "No file selected", 400

    f = request.files["file"]
    in_path = os.path.join(app.config["UPLOAD_FOLDER"], f.filename)
    f.save(in_path)

    out_html = os.path.join(app.config["UPLOAD_FOLDER"], "output.html")

    page_raw = request.form.get("page", "1")
    page_nr = int(page_raw)

    os.system(f'python src/main.py "{in_path}" "{out_html}" {page_nr}')

    return render_template(
        "download.html", file_url=f"/download?filename={os.path.basename(out_html)}"
    )


@app.route("/download")
def download():
    fname = request.args.get("filename", "")
    return send_file(os.path.join(UPLOAD_FOLDER, fname), as_attachment=True)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/domxss")
def domxss():
    return render_template("domxss.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
