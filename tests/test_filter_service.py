from app.schemas.job import Job
from app.services.filter_service import FilterService


def test_filter_allows_job():
    service = FilterService()

    job = Job(
        title="Backend Developer",
        company="Test",
        url="https://example.com/job",
        location="Remote",
        description="Junior Python developer",
        source="test",
    )

    assert service.is_allowed(job) is True


def test_filter_blocks_excluded_keyword():
    service = FilterService()

    service.excluded_keywords = ["marketing"]

    job = Job(
        title="Marketing Manager",
        company="Test",
        url="https://example.com/job-2",
        location="Remote",
        description="Digital marketing specialist",
        source="test",
    )

    assert service.is_allowed(job) is False