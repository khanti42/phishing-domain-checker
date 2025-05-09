# Phishing Domain Checker

A Python-based tool that automates the verification of domains against MetaMask's phishing detection lists. It classifies domains into `allowlist`, `blocklist`, `fuzzylist`, or `unknown` based on the latest data from MetaMask's API.

## 🚀 Features

- **Automated List Retrieval**: Fetches the latest `allowlist`, `blocklist`, and `fuzzylist` from MetaMask's phishing detection API.
- **Domain Classification**: Analyzes input URLs and classifies their top-level domains accordingly.
- **Fuzzy Matching**: Implements approximate string matching to identify domains similar to known phishing sites.
- **Batch Processing**: Supports processing multiple URLs efficiently.

## 🛠️ Prerequisites

- **Python 3.7 or higher**
- **Required Python Packages**:
  - `requests`
  - `tldextract`
  - `difflib` (standard library)

## 📦 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/phishing-domain-checker.git
   cd phishing-domain-checker
   ```

2. **Create a Virtual Environment (Optional but Recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 📈 Usage

1. **Prepare Your List of URLs**:
   Create a text file (e.g., `urls.txt`) containing one URL per line.

2. **Run the Script**:
   ```bash
   python phishing_checker.py urls.txt
   ```

3. **View Results**:
   The script will output the classification for each URL in the console.

## 🧪 Example

Given an `urls.txt` file with the following content:

```text
https://opensea.io
https://cryptokitties.co
https://cham-transfers.com
https://unknownsite.example
```

Running the script will yield:

```text
https://opensea.io: allowlist
https://cryptokitties.co: fuzzylist
https://cham-transfers.com: blocklist
https://unknownsite.example: unknown
```

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

## 📄 License

This project is licensed under the MIT License. 

## ⚙️ Repository Setup Steps

To set up the repository locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/phishing-domain-checker.git
   cd phishing-domain-checker
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Your URLs File**:
   Create a text file named `urls.txt` and list the URLs you want to check, one per line.

5. **Run the Script**:
   ```bash
   python phishing_checker.py urls.txt
   ```

6. **Review the Output**:
   The script will display the classification results for each URL in the console.