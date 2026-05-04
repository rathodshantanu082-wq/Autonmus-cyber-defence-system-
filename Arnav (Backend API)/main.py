from fastapi import FastAPI
from backend.api.routes_monitor import router as monitor_router
from backend.api.route_simulation import router as simulation_router

app = FastAPI(title="Autonomous Cyber Defence System")

app.include_router(monitor_router, prefix="/monitor")
app.include_router(simulation_router, prefix="/simulate")

@app.get("/")
def home():
    return {"message": "Cyber Defence System Running"}