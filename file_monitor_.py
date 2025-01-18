import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
import time

# Configuration (Replace with your actual details)
SENDER_EMAIL = "your_email@gmail.com"  # Sender's email address
SENDER_PASSWORD = "your_generated_app_password"  # Use your generated app password from Gmail
RECEIVER_EMAIL = "receiver_email@gmail.com"  # Recipient's email address
MONITOR_PATH = "C:/path/to/monitor"  # Directory to monitor (change this to the correct folder)
LOG_FILE = "file_monitor_log.txt"  # Path to the log file where events will be saved

# Setup logging to track file changes in a log file
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,  # Set logging level to INFO (can be changed to DEBUG for more detailed logs)
    format='%(asctime)s - [%(levelname)s] - %(message)s'  # Log format with timestamps
)

logging.info("File monitoring system initialized.")  # Initial log entry to mark system startup


# Function to send email alerts when a file event occurs
def send_email_alert(event_type, file_path):
    subject = f"File {event_type.capitalize()} Alert"  # Subject of the email
    body = f"""
    <html>
    <body>
        <h3>File Monitoring Alert</h3>
        <p>A file event was detected:</p>
        <table border="1">
            <tr><th>Event Type</th><td>{event_type.capitalize()}</td></tr>  # Event type (created, modified, deleted)
            <tr><th>File Path</th><td>{file_path}</td></tr>  # The file path where the change occurred
            <tr><th>Timestamp</th><td>{time.ctime()}</td></tr>  # Timestamp of when the event occurred
        </table>
    </body>
    </html>
    """

    message = MIMEMultipart()  # Create a multipart email message
    message['From'] = SENDER_EMAIL  # Sender's email address
    message['To'] = RECEIVER_EMAIL  # Recipient's email address
    message['Subject'] = subject  # Email subject
    message.attach(MIMEText(body, 'html'))  # Attach the email body as HTML

    # Attach the log file to the email
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')  # Define the MIME type for the file attachment
            part.set_payload(attachment.read())  # Read the log file
            encoders.encode_base64(part)  # Encode the file in base64
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={os.path.basename(LOG_FILE)}'  # Attach the log file with the name from the log file path
            )
            message.attach(part)  # Attach the log file to the email

    try:
        # Connect to Gmail's SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Log in with the sender's credentials
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())  # Send the email
            logging.info("Email alert sent successfully.")  # Log that the email was sent successfully
    except Exception as e:
        logging.error(f"Failed to send email: {e}")  # Log any errors that occur during the email sending process


# Function to check if the file is hidden (e.g., Thumbs.db, .DS_Store)
def is_hidden(file_path):
    return file_path.startswith('.') or (os.name == 'nt' and file_path.lower() == 'thumbs.db')


# File monitoring handler to handle different types of file system events
class MonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        """Trigger when a file is modified"""
        if not event.is_directory and not is_hidden(event.src_path):  # Ensure the file isn't hidden or a directory
            logging.info(f"File modified: {event.src_path}")  # Log the modification
            send_email_alert('modified', event.src_path)  # Send email alert for the modification

    def on_created(self, event):
        """Trigger when a file is created"""
        if not event.is_directory and not is_hidden(event.src_path):  # Ensure the file isn't hidden or a directory
            logging.info(f"File created: {event.src_path}")  # Log the creation
            send_email_alert('created', event.src_path)  # Send email alert for the creation

    def on_deleted(self, event):
        """Trigger when a file is deleted"""
        if not event.is_directory and not is_hidden(event.src_path):  # Ensure the file isn't hidden or a directory
            logging.info(f"File deleted: {event.src_path}")  # Log the deletion
            send_email_alert('deleted', event.src_path)  # Send email alert for the deletion


# Main function to start the file monitoring system
def main():
    # Ensure the directory to monitor exists
    if not os.path.exists(MONITOR_PATH):
        print(f"Error: Monitor path does not exist: {MONITOR_PATH}")  # Display error if directory doesn't exist
        logging.error(f"Monitor path does not exist: {MONITOR_PATH}")  # Log the error
        return

    print(f"Monitoring directory: {MONITOR_PATH}")  # Print which directory is being monitored
    logging.info(f"Monitoring directory: {MONITOR_PATH}")  # Log the directory being monitored

    # Initialize the observer to monitor file system changes
    observer = Observer()
    handler = MonitorHandler()  # Instantiate the handler that will process file events
    observer.schedule(handler, path=MONITOR_PATH, recursive=False)  # Start monitoring the directory (non-recursively)
    observer.start()  # Start the observer to begin monitoring

    try:
        while True:
            time.sleep(1)  # Keep the script running indefinitely
    except KeyboardInterrupt:
        observer.stop()  # Stop the observer gracefully when interrupted by the user
        logging.info("Monitoring stopped by user.")  # Log that monitoring was stopped by the user
        print("Monitoring stopped.")  # Print a message indicating monitoring was stopped
    observer.join()  # Wait for the observer to finish before closing the program


if __name__ == "__main__":
    main()  # Start the program
