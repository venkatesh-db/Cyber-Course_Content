
def detection_brutforce(logs):
    print("Detecting brute force attacks...")
        
    failed_count ={}
    
    for log in logs:
        if log["event_id"] == 4625:
            ip = log["ip"]
            failed_count[ip] = failed_count.get(ip, 0) + 1
            
    alerts = []
    for ip, count in failed_count.items():
        if count == 3:
            alerts.append(
                {
                    "type": "Brute Force Attack",
                    "ip": ip,
                    "attempts": count
                }
            )
            
    
    return alerts

