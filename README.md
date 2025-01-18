# 🚨 File Integrity Monitoring System with Python: Real-Time Alerts & Monitoring 🔒💻

In today's digital landscape, file integrity is crucial for securing sensitive data and preventing unauthorized access. This **File Integrity Monitoring System** continuously monitors directories for any **file changes** (creation, modification, or deletion) and automatically sends **email alerts** when suspicious activity is detected.

This tool is ideal for businesses and individuals who want to ensure the integrity of their files and prevent data breaches or unauthorized file changes.

### Key Highlights:
- **📂 Real-Time Monitoring**: Tracks changes in files and directories as they happen.
- **🔔 Instant Email Alerts**: Get notified immediately when files are created, modified, or deleted.
- **📜 Detailed Logs**: Keeps track of all events for future reference and analysis.
- **🛡️ Enhanced Security**: Ideal for securing critical files and sensitive data.

### Technologies Used:
- **Python**: Used the **Watchdog** library for file system monitoring.
- **Email Automation (SMTP)**: Integrated **Gmail SMTP** to send notifications.
- **Logging**: Added robust logging for real-time event tracking.

### Prerequisites:
- Python 3.x
- **Watchdog** library: This is used for monitoring file system changes.
  
To install the required libraries, run:

```bash
pip install watchdog
