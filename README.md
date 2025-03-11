# SuperRansomware - Educational Cybersecurity Research Tool

## ⚠ Disclaimer
**This project is strictly for educational and research purposes.** It is designed to help cybersecurity professionals and ethical hackers understand ransomware behavior, analyze attack vectors, and develop better defense mechanisms. **Misuse of this tool for illegal activities is strictly prohibited.**

## 📌 About the Project
SuperRansomware is a cybersecurity research tool designed to simulate ransomware attacks in a controlled environment. The purpose of this project is to analyze file encryption techniques, study how attackers operate, and develop mitigation strategies.

## 🚀 Features
- Detects available drives on a system.
- Scans for specific file types.
- Simulates file encryption using modern cryptographic methods.
- Sends encryption keys to a specified remote server for analysis.
- Drops a notification file to demonstrate the ransomware behavior.

## 🎯 Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SuperRansomware.git
   cd SuperRansomware
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. **Modify the webhook URL** in the script (**Line 121**) to point to your own controlled server for key analysis before execution.
4. Convert the script to an executable for testing in a controlled lab environment:
   ```bash
   pyinstaller --onefile ransomware.py
   ```

## 🔬 Research & Analysis
Security analysts can use this tool to:
- Examine how ransomware spreads and encrypts files.
- Develop and test decryption methods.
- Create effective security policies to mitigate real-world attacks.
- Analyze forensic artifacts left by ransomware infections.

## ⚠ Important Notes
- **Do not run this tool on any unauthorized system.**
- **Only test in a virtual machine or isolated lab environment.**
- **Do not distribute malicious versions of this tool.**

## 🛡 Legal & Ethical Responsibility
This project is intended for ethical hacking, security research, and penetration testing under legal conditions. Any unauthorized or illegal use of this tool is solely the user's responsibility.

## 📫 Contact
For inquiries related to ethical hacking and cybersecurity research, contact:
📧 matinnoryan@gmail.com
 

---
**Educational Purposes Only - Do Not Use for Malicious Intent**
#### Matitanium
