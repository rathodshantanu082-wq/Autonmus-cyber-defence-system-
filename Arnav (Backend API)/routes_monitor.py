from fastapi import APIRouter
from backend.api.monitor import generate_logs, detect_bruteforce

router = APIRouter()

@router.get("/logs")
def get_logs():
    logs = generate_logs()
    return {"logs": logs}


@router.get("/detect")
def detect_threats():
    logs = generate_logs()
    suspicious = detect_bruteforce(logs)

    return {
        "logs": logs,
        "suspicious_ips": suspicious
    }