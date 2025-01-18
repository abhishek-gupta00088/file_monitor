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

Configure the Script:
Update the following variables in the script with your own details:

SENDER_EMAIL: Your email address (e.g., your_email@gmail.com).
SENDER_PASSWORD: The app password generated from Gmail (if using 2FA).
RECEIVER_EMAIL: The email address where you want to receive notifications.
MONITOR_PATH: The directory you want to monitor for file changes.
LOG_FILE: Path to the log file where events will be stored.
How It Works:
The Watchdog library monitors the specified directory for changes. It detects:

File Creation
File Modification
File Deletion
Whenever a change is detected, the script sends an email notification using Gmail's SMTP server. The email contains details about the event (e.g., file path, event type, timestamp). All events are logged into a file, providing a history of all changes that have occurred in the monitored directory.

How to Run the Script:
Run the script by executing the following command in your terminal:

bash
Copy
Edit
python file_monitor.py
Monitor the output: The script will start monitoring the specified directory for any file events. It will log these events and send email alerts as changes occur.

Example Output:
Terminal Output:

bash
Copy
Edit
Monitoring directory: C:/path/to/monitor
File modified: C:/path/to/monitor/test_file.txt
File created: C:/path/to/monitor/new_file.txt
File deleted: C:/path/to/monitor/old_file.txt
Email Example:

Subject: File Created Alert
Body:
yaml
Copy
Edit
A file has been created: C:/path/to/monitor/new_file.txt
Timestamp: Fri Jan 18 2025 12:00:00
With this tool, file integrity can be ensured by detecting unauthorized changes and preventing potential data loss or breaches. This is critical for:

Network Security: Keeping track of file changes within the network.
Data Protection: Ensuring files remain unchanged and secure.
System Administration: Monitoring files in system-critical directories.
This tool is a must-have for businesses or individuals who handle sensitive information and require real-time alerts to protect their data.

Feel free to contribute to this project! If you have suggestions or improvements, open an issue or submit a pull request. Contributions are always welcome! 🙌

This project is licensed under the MIT License - see the LICENSE file for details.

Final Thoughts:
This File Integrity Monitoring System is a simple yet powerful solution for ensuring the security of files and directories. By leveraging Python and real-time monitoring, this tool helps keep critical data safe and gives peace of mind with automated alerts.
