from app.schemas.job import Job
from app.services.scoring_service import ScoringService


def test_scoring_high_match():
    service = ScoringService()

    job = Job(
        title="Junior Backend Developer",
        company="Test",
        url="https://example.com/job",
        location="Remote",
        description=(
            "Python FastAPI developer working with "
            "REST API, SQL, Docker and AWS."
        ),
        source="test",
    )

    result = service.score(job)

    assert result.score == 100
    assert result.recommendation == "high"


def test_scoring_low_match():
    service = ScoringService()

    job = Job(
        title="Marketing Manager",
        company="Test",
        url="https://example.com/job-2",
        location="Bogota",
        description="Marketing and advertising specialist.",
        source="test",
    )

    result = service.score(job)

    assert result.score == 0
    assert result.recommendation == "low"