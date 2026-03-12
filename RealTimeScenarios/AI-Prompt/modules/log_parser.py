import pandas as pd

class LogParser:
    def parse(self, log_file):
        """Parse log file and return a pandas DataFrame."""
        log_entries = []
        with open(log_file, "r") as file:
            for line in file:
                log_entries.append({"raw": line.strip()})
        return pd.DataFrame(log_entries)