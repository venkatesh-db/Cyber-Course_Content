

# source ransomware_env/bin/activate
# python ransomware_detection.py
# Enter the directory to monitor: /Users/venkatesh/Downloads

'''

source ransomware_env/bin/activate
python3 ransomware_detection.py

directory - /Users/venkatesh/Downloads
ls /Users/venkatesh/Downloads

touch /Users/venkatesh/Downloads/testfile.txt
echo "Hello" >> /Users/venkatesh/Downloads/testfile.txt
rm /Users/venkatesh/Downloads/testfile.txt




'''



import os
import time
import hashlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RansomwareDetectionHandler(FileSystemEventHandler):
    def __init__(self, monitored_dir, alert_callback):
        self.monitored_dir = monitored_dir
        self.alert_callback = alert_callback
        self.file_hashes = {}

    def calculate_hash(self, file_path):
        """Calculate the hash of a file."""
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            return file_hash
        except Exception as e:
            return None

    def on_modified(self, event):
        """Triggered when a file is modified."""
        if not event.is_directory:
            file_path = event.src_path
            new_hash = self.calculate_hash(file_path)
            if file_path in self.file_hashes:
                if self.file_hashes[file_path] != new_hash:
                    print(f"[ALERT] File modified: {file_path}")
                    self.alert_callback(file_path, "File modified suspiciously")
            self.file_hashes[file_path] = new_hash

    def on_created(self, event):
        """Triggered when a new file is created."""
        if not event.is_directory:
            file_path = event.src_path
            print(f"[INFO] New file created: {file_path}")
            self.file_hashes[file_path] = self.calculate_hash(file_path)

    def on_deleted(self, event):
        """Triggered when a file is deleted."""
        if not event.is_directory:
            file_path = event.src_path
            print(f"[ALERT] File deleted: {file_path}")
            self.alert_callback(file_path, "File deleted suspiciously")

def alert_callback(file_path, message):
    """Handle alerts for suspicious activities."""
    print(f"[ALERT] Suspicious activity detected: {message} - {file_path}")

def monitor_directory(directory):
    """Monitor a directory for ransomware-like activities."""
    event_handler = RansomwareDetectionHandler(directory, alert_callback)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()
    print(f"Monitoring directory: {directory}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitored_directory = input("Enter the directory to monitor: ")
    if os.path.isdir(monitored_directory):
        monitor_directory(monitored_directory)
    else:
        print("Invalid directory. Please provide a valid path.")