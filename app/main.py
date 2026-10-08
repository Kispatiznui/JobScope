from fastapi import FastAPI

from app.api.routes.jobs import router as jobs_router
from app.services.config_service import load_profile
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title="JobScope",
    description="Configurable job analysis backend",
    version="0.1.0",
)

app.include_router(jobs_router)


@app.get("/")
def root():
    profile = load_profile()

    return {
        "name": "JobScope",
        "status": "running",
        "version": "0.1.0",
        "profile": profile["name"],
    }