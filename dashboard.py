from flask import Flask, render_template
import os
import json

app = Flask(__name__)
OUTPUT_DIR = "output"
BLOCKLIST_FILE = os.path.join(OUTPUT_DIR, "blocklists.json")
REPORT_FILE = os.path.join(OUTPUT_DIR, "ioc_report.json")

def load_data():
    if not os.path.exists(BLOCKLIST_FILE) or not os.path.exists(REPORT_FILE):
        return {}, {}
    with open(BLOCKLIST_FILE) as f:
        blocklists = json.load(f)
    with open(REPORT_FILE) as f:
        report = json.load(f)
    return blocklists, report

@app.route("/")
def index():
    blocklists, report = load_data()
    return render_template("dashboard.html",
                           blocklists=blocklists,
                           report=report)

if __name__ == "__main__":
    app.run(debug=True)
