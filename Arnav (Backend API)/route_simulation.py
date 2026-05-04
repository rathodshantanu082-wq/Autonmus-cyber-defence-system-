from fastapi import APIRouter
from backend.api.simulator import simulate_attack

router = APIRouter()

@router.get("/attack")
def simulate():
    return simulate_attack()