# File Integrity Monitoring System with Python

The **File Integrity Monitoring System** is a Python-based tool that continuously monitors a specified directory for **file changes** such as **creation**, **modification**, or **deletion**. It helps ensure the integrity of critical files by sending **real-time email notifications** whenever any changes occur.

This tool is perfect for individuals or businesses that want to monitor sensitive data or system-critical files for unauthorized changes or accidental modifications.

## Features:
- **📂 Real-Time Monitoring**: Monitors a specific directory for changes to any file.
- **🔔 Email Alerts**: Sends instant email notifications when files are created, modified, or deleted.
- **📜 Detailed Event Logging**: Keeps track of all file changes with timestamps for future reference and security auditing.
- **🛡️ Enhanced File Security**: Helps ensure the integrity of important files, preventing unauthorized alterations.

## Purpose:
This project helps users maintain the **integrity and security** of files and directories by tracking file changes and sending immediate alerts. It is particularly useful for:
- **Data Protection**: Ensuring sensitive data remains untouched and secure.
- **Network Security**: Keeping an eye on critical files that could be at risk of unauthorized access or tampering.
- **System Administration**: Monitoring system files for any unexpected modifications, especially on servers or systems that require a high level of security.

## How It Works:
- The **Watchdog** library is used to monitor file system events in real-time.
- The script detects changes in the specified directory, such as when files are created, modified, or deleted.
- When an event occurs, the script sends an email with the details of the change, including:
  - The file path
  - The type of event (create, modify, or delete)
  - A timestamp of when the change occurred
- All events are logged into a text file for future reference and analysis.

This system can be customized to monitor specific directories, track particular types of file changes, and send alerts to the specified email address.

## Use Cases:
- **Security Auditing**: Track changes in sensitive directories or files, ensuring compliance with security policies.
- **Backup and Restore**: Monitor files for modifications and ensure that backups are made regularly.
- **System Monitoring**: Watch critical system directories for unauthorized changes, protecting against malware or human error.

This tool gives you peace of mind by ensuring that any changes to important files are detected and reported in real time, reducing the risk of data loss or security breaches.

## How to Run:
To run the script, simply execute it in your Python environment. It will start monitoring the specified directory and send notifications upon detecting any changes.
