from pathlib import Path
import requests
import tldextract
import difflib
import argparse
import json
import csv
import sys

# Constants
DEFAULT_INPUT_FILE = "urls.txt"
DEFAULT_OUTPUT_FORMAT = "terminal"
SUPPORTED_FORMATS = ["terminal", "json", "csv"]
PHISHING_API_URL = "https://phishing-detection.api.cx.metamask.io/v1/stalelist"

# Step 1: Fetch the lists from MetaMask API
def fetch_lists():
    try:
        response = requests.get(PHISHING_API_URL)
        response.raise_for_status()
        data = response.json().get("data", {})
        return set(data.get("allowlist", [])), set(data.get("fuzzylist", [])), set(data.get("blocklist", []))
    except requests.RequestException as e:
        print(f"Error fetching phishing lists: {e}")
        sys.exit(1)

# Step 2: Extract the top-level domain from a URL
def extract_domain(url):
    extracted = tldextract.extract(url)
    return f"{extracted.domain}.{extracted.suffix}"

# Step 3: Classify the domain
def classify_domain(domain, allowlist, blocklist, fuzzylist):
    if domain in allowlist:
        return "allowlist"
    elif domain in blocklist:
        return "blocklist"
    elif difflib.get_close_matches(domain, fuzzylist, n=1, cutoff=0.8):
        return "fuzzylist"
    else:
        return "unknown"

# Output writers
def output_terminal(results):
    for url, data in results.items():
        print(f"{url}: {data['domain']} => {data['classification']}")

def output_json(results, filename="results.json"):
    with open(filename, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {filename}")

def output_csv(results, filename="results.csv"):
    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "Domain", "Classification"])
        for url, data in results.items():
            writer.writerow([url, data["domain"], data["classification"]])
    print(f"Results saved to {filename}")

# Argument parsing
def parse_args():
    parser = argparse.ArgumentParser(description="Classify URLs using MetaMask's phishing detection lists.")
    parser.add_argument("input", nargs="?", default=DEFAULT_INPUT_FILE, help="Input file containing URLs (default: urls.txt)")
    parser.add_argument("--output", choices=SUPPORTED_FORMATS, default=DEFAULT_OUTPUT_FORMAT,
                        help="Output format: terminal, json, or csv (default: terminal)")
    return parser.parse_args()

# Main script
def main():
    args = parse_args()

    if not Path(args.input).exists():
        print(f"Error: Input file '{args.input}' not found.")
        sys.exit(1)

    with open(args.input, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    allowlist, fuzzylist, blocklist = fetch_lists()
    results = {}
    has_threat_detected = False

    for url in urls:
        domain = extract_domain(url)
        classification = classify_domain(domain, allowlist, blocklist, fuzzylist)
        results[url] = {"domain": domain, "classification": classification}
        if classification in ("fuzzylist", "blocklist"):
            has_threat_detected = True

    if args.output == "terminal":
        output_terminal(results)
    elif args.output == "json":
        output_json(results)
    elif args.output == "csv":
        output_csv(results)

    sys.exit(2 if has_threat_detected else 0)

main()
