from app.schemas.job import Job
from app.services.matching_service import MatchingService


def test_matching_backend_developer():
    service = MatchingService()

    job = Job(
        title="Backend Developer",
        company="Test",
        url="https://example.com/job",
        location="Remote",
        description="Junior Python developer",
        source="test",
    )

    assert service.matches(job) is True


def test_matching_normalizes_job_text():
    service = MatchingService()

    job = Job(
        title="Backend-Developer",
        company="Test",
        url="https://example.com/job-2",
        location="REMOTE",
        description="Junior Python developer",
        source="test",
    )

    assert service.matches(job) is True