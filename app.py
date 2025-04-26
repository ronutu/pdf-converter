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
    # naïve blacklist – decode *after* the check → bypass with "..%2
    if "../" in raw_name or "%2e" in raw_name.lower():
        return "❌ Suspicious filename", 400

    filename = urllib.parse.unquote(raw_name)  # decode only now
    file_path = os.path.join(BASE_DIR, filename)  # attacker controls this
    try:
        return send_file(file_path)
    except FileNotFoundError:
        return "❌ File not found", 404


# ---------------------------------------------------------------------------
# 2. *Command-injection* via unsanitised file name
# ---------------------------------------------------------------------------
@app.route("/run-script", methods=["POST"])
def run_script():
    # User is *expected* to smuggle shell metacharacters here
    filename = request.form.get("filename", "")
    # Run conversion script (path fixed) …
    os.system("python src/main.py")
    # …and blindly echo the user-supplied value (vulnerability!)
    output = getoutput(f"echo {filename}")
    return f"<pre>{output}</pre>"


# ---------------------------------------------------------------------------
# 3. *SSTI* – raw Jinja2 template execution
# ---------------------------------------------------------------------------
@app.route("/render", methods=["GET", "POST"])
def unsafe_render():
    user_content = request.values.get("content", "")
    return render_template_string(user_content)  # {{ self.__class__.mro() }}


# ---------------------------------------------------------------------------
# 4. *SQL-injection* – dangerous string interpolation in WHERE clause
# ---------------------------------------------------------------------------
@app.route("/logs")
def logs():
    query = request.args.get("query", "1=1")  # attacker controls WHERE
    conn = sqlite3.connect("logs.db")
    cur = conn.cursor()
    rows = cur.execute(f"SELECT * FROM logs WHERE {query}").fetchall()
    conn.close()
    return render_template_string(
        "<ul>{% for r in rows %}<li>{{ r }}</li>{% endfor %}</ul>", rows=rows
    )


# ---------------------------------------------------------------------------
# 5. *Reflected XSS*
# ---------------------------------------------------------------------------
@app.route("/xss")
def xss():
    user_input = request.args.get("input", "")
    return f"<p>{user_input}</p>"  # no escaping – enjoy! :)


# ---------------------------------------------------------------------------
# 6. Upload + automatic conversion (uses whatever you already wrote)
# ---------------------------------------------------------------------------
# ─── app.py  (only the /upload view needs a tweak) ────────────────────────────
@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files or request.files["file"].filename == "":
        return "No file selected", 400

    f = request.files["file"]
    in_path = os.path.join(app.config["UPLOAD_FOLDER"], f.filename)
    f.save(in_path)

    out_html = os.path.join(app.config["UPLOAD_FOLDER"], "output.html")

    # NEW: grab the number; default to 1
    page_raw = request.form.get("page", "1")
    # (we *deliberately* skip robust validation because the whole app is a lab)
    page_nr = int(page_raw)

    # main.py expects:  python src/main.py <pdf> <html>   <page_nr>
    os.system(f'python src/main.py "{in_path}" "{out_html}" {page_nr}')

    return render_template(
        "download.html", file_url=f"/download?filename={os.path.basename(out_html)}"
    )


@app.route("/download")
def download():
    fname = request.args.get("filename", "")
    return send_file(os.path.join(UPLOAD_FOLDER, fname), as_attachment=True)


# ---------------------------------------------------------------------------
#  Simple pages & helpers
# ---------------------------------------------------------------------------
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/domxss")
def domxss():
    return render_template("domxss.html")


if __name__ == "__main__":
    # Debug mode *on purpose* so Werkzeug exposes the interactive console
    app.run(debug=True, host="0.0.0.0", port=5000)
