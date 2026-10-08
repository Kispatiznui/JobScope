from fastapi import APIRouter

from app.schemas.job import Job
from app.services.job_service import JobService


router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.get("/", response_model=list[Job])
def get_jobs():
    service = JobService()

    return service.get_jobs()