import os
import json

def collect_logs(log_directory):
    """
    Collect logs from the specified directory.

    Args:
        log_directory (str): Path to the directory containing log files.

    Returns:
        list: A list of log entries.
    """
    logs = []
    try:
        for filename in os.listdir(log_directory):
            if filename.endswith('.log'):
                file_path = os.path.join(log_directory, filename)
                with open(file_path, 'r') as file:
                    for line in file:
                        try:
                            log_entry = json.loads(line.strip())
                            logs.append(log_entry)
                        except json.JSONDecodeError:
                            print(f"Invalid JSON in file {filename}: {line.strip()}")
    except FileNotFoundError:
        print(f"Log directory not found: {log_directory}")
    except Exception as e:
        print(f"Error collecting logs: {e}")

    return logs

if __name__ == "__main__":
    # Example usage
    log_dir = "../data_sources/payment_logs"
    collected_logs = collect_logs(log_dir)
    print(f"Collected {len(collected_logs)} log entries.")