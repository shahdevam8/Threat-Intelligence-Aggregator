import os
import re
import json
import ipaddress
from datetime import datetime

FEED_DIR = "feeds"
OUTPUT_DIR = "output"
BLOCKLIST_FILE = os.path.join(OUTPUT_DIR, "blocklists.json")
REPORT_FILE = os.path.join(OUTPUT_DIR, "ioc_report.json")

# Regex patterns
IP_PATTERN = re.compile(r"(?:\d{1,3}\.){3}\d{1,3}")
DOMAIN_PATTERN = re.compile(r"(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}")
URL_PATTERN = re.compile(r"https?://[^\s]+")
HASH_PATTERN = re.compile(r"\b[a-fA-F0-9]{32,64}\b")
EMAIL_PATTERN = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}\b")

class ThreatIntelAggregator:
    def __init__(self):
        self.ips = set()
        self.domains = set()
        self.urls = set()
        self.hashes = set()
        self.emails = set()
        self.feed_summary = {}

    def load_feeds(self):
        if not os.path.exists(FEED_DIR):
            os.makedirs(FEED_DIR)
            print(f"Created feed folder: {FEED_DIR}. Add sample feeds to run.")
            return

        files = os.listdir(FEED_DIR)
        if not files:
            print("No feed files found in feeds/. Add sample feeds first.")
            return

        for filename in files:
            path = os.path.join(FEED_DIR, filename)
            with open(path, "r") as f:
                content = f.read()
                self.parse_indicators(content)
                self.feed_summary[filename] = len(content.splitlines())

    def parse_indicators(self, text):
        self.ips.update(IP_PATTERN.findall(text))
        self.domains.update(DOMAIN_PATTERN.findall(text))
        self.urls.update(URL_PATTERN.findall(text))
        self.hashes.update(HASH_PATTERN.findall(text))
        self.emails.update(EMAIL_PATTERN.findall(text))

    def save_blocklists(self):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        blocklists = {
            "ips": sorted(list(self.ips)),
            "domains": sorted(list(self.domains)),
            "urls": sorted(list(self.urls)),
            "hashes": sorted(list(self.hashes)),
            "emails": sorted(list(self.emails))
        }

        with open(BLOCKLIST_FILE, "w") as f:
            json.dump(blocklists, f, indent=4)

    def save_report(self):
        report = {
            "total_indicators": {
                "ips": len(self.ips),
                "domains": len(self.domains),
                "urls": len(self.urls),
                "hashes": len(self.hashes),
                "emails": len(self.emails)
            },
            "feed_summary": self.feed_summary,
            "timestamp": datetime.now().isoformat()
        }

        with open(REPORT_FILE, "w") as f:
            json.dump(report, f, indent=4)

    def run(self):
        self.load_feeds()
        self.save_blocklists()
        self.save_report()
        print("Feeds processed. Blocklists and reports generated.")

if __name__ == "__main__":
    tia = ThreatIntelAggregator()
    tia.run()
