import random

def simulate_attack():
    attacks = [
        "Brute Force Attack",
        "DDoS Attempt",
        "Port Scanning",
        "Malware Activity"
    ]

    return {
        "attack_type": random.choice(attacks),
        "severity": random.choice(["Low", "Medium", "High"])
    }