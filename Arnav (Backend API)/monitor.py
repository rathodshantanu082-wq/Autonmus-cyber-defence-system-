import random
from backend.api.logger import logger

# Simulated system logs
def generate_logs():
    sample_logs = []
    for _ in range(10):
        log = {
            "ip": f"192.168.1.{random.randint(1, 255)}",
            "status": random.choice(["success", "failed"])
        }
        sample_logs.append(log)
    return sample_logs


# Simple brute-force detection
def detect_bruteforce(logs):
    failed_attempts = {}

    for log in logs:
        if log["status"] == "failed":
            ip = log["ip"]
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    suspicious = [ip for ip, count in failed_attempts.items() if count > 3]

    if suspicious:
        logger.warning(f"Suspicious IPs detected: {suspicious}")

    return suspicious