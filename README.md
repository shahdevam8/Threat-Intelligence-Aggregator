# Threat Intelligence Aggregator (Non-AI) - README

## Project Overview

The **Threat Intelligence Aggregator (TIA)** is a practical cybersecurity tool designed to collect, parse, normalize, and correlate threat intelligence indicators from multiple external and internal feeds without using AI or machine learning. It generates actionable blocklists and reports to strengthen your security posture.

Modern cybersecurity relies heavily on accurate and real-time threat intelligence. Indicators of Compromise (IOCs) such as malicious IPs, URLs, domains, file hashes, and email addresses are often distributed across different sources with inconsistent formats. TIA standardizes these feeds, identifies repeated or high-risk indicators, and produces exportable blocklists.

---

## Features

* Supports multiple IOC feed formats: CSV, TXT, JSON
* Extracts IPs, domains, URLs, file hashes, emails
* Deduplicates and normalizes indicators
* Correlates repeated indicators across feeds
* Generates severity ratings for high-frequency threats
* Produces blocklists for firewalls, EDR, web filters
* Generates summary reports for monitoring and SOC teams

---

## How it Solves Problems

TIA addresses common challenges in threat intelligence:

1. **Feed inconsistency:** Automatically parses multiple formats.
2. **Redundant indicators:** Correlates and deduplicates repeated IOCs.
3. **Manual reporting:** Produces automated blocklists and reports.
4. **Prioritization:** Highlights high-risk indicators based on cross-feed occurrences.
5. **SOC readiness:** Output can be directly used in security tools.

---

## Tools & Technologies Used

* **Programming Language:** Python 3.x
* **Libraries:**

  * `os`, `re` (file and pattern handling)
  * `json`, `csv` (feed parsing)
  * `requests` (fetching online feeds)
  * `ipaddress` (IP validation)
  * `hashlib` (hash validation)

---

## Folder Structure

```
Threat-Intelligence-Aggregator/
├── aggregator.py       # Main Python script
├── dashboard.py
├── report_generator.py
├── utils.py
├── feeds/              # Directory containing IOC feed files (TXT, CSV, JSON)
│   ├── sample.txt
│   ├── sample.csv
│   └── sample.json
├── output/             # Generated outputs
│   ├── blocklists/     # Blocklists by type (IPs, domains, URLs, hashes, emails)
│   └── report.txt      # Summary report
└── requirements.txt    # Python dependencies
```

---

## Installation

1. Clone or download the project.
2. Install required libraries:

```bash
pip install -r requirements.txt
```

**requirements.txt:**

```
requests
stix2
ipaddress
```

*(You can add more libraries if needed, e.g., `pandas` for advanced CSV processing.)*

---

## Usage Guide

1. Place IOC feed files inside the `feeds/` folder.
2. Run the aggregator:

```bash
python aggregator.py
```

3. Outputs are generated in the `output/` folder:

   * `output/blocklists/ips.txt`
   * `output/blocklists/domains.txt`
   * `output/blocklists/urls.txt`
   * `output/blocklists/hashes.txt`
   * `output/blocklists/emails.txt`
   * `output/report.txt`

### Example Feed

`feeds/sample.txt`:

```
192.168.1.100
malicious.com
user@evil.com
```

`feeds/sample.csv`:

```
bad.com,10.0.0.5,abcd1234abcd1234abcd1234abcd1234
```

`feeds/sample.json`:

```json
[
    "http://phishing-site.com/login",
    "192.168.1.100",
    "abcdefabcdefabcdefabcdefabcdefabcd"
]
```

### Example Output

`output/blocklists/ips.txt`:

```
10.0.0.5
192.168.1.100
```

`output/report.txt` contains a summary of unique indicators, occurrences across feeds, and high-risk items.

---

## How it Helps the User

* **Security teams**: Quickly generate blocklists and reports from multiple threat feeds.
* **SOC Analysts**: Identify repeated or high-risk threats and prioritize response.
* **Defensive automation**: Outputs can be integrated with firewalls, IDS, and endpoint tools.
* **Learning & experimentation**: Understand IOC structures, normalization, and correlation workflows.

---

## Practical Workflow

1. **Load Feeds** – Load CSV, TXT, JSON feeds.
2. **Parse Indicators** – Extract IPs, URLs, domains, hashes, emails.
3. **Normalize Data** – Deduplicate and standardize.
4. **Correlation Engine** – Detect repeated/high-frequency IOCs.
5. **Blocklist Generation** – Generate per-category files.
6. **Reporting** – Produce human-readable summary of feed processing and results.

---

## Notes

* Ensure the `feeds/` folder exists before running.
* Regularly update your feeds for accurate intelligence.
* Validate outputs before deploying to production security tools.
