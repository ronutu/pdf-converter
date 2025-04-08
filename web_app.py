from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run")
def run_script():
    subprocess.Popen(["python", "src/main.py"])
    return "Script started!"

if __name__ == "__main__":
    app.run(debug=True)