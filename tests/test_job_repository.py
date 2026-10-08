from app.repositories.job_repository import JobRepository
from app.schemas.job import Job


def create_job(url: str) -> Job:
    return Job(
        title="Backend Developer",
        company="Test",
        url=url,
        location="Remote",
        description="Junior Python developer",
        salary=None,
        source="test",
        score=80,
        recommendation="high",
    )


def test_repository_saves_and_gets_jobs(tmp_path):
    database_path = tmp_path / "test.db"

    repository = JobRepository(str(database_path))

    job = create_job("https://example.com/job")

    repository.save_jobs([job])

    jobs = repository.get_all()

    assert len(jobs) == 1
    assert jobs[0].title == "Backend Developer"
    assert jobs[0].company == "Test"
    assert jobs[0].url == "https://example.com/job"
    assert jobs[0].score == 80
    assert jobs[0].recommendation == "high"


def test_repository_prevents_duplicate_urls(tmp_path):
    database_path = tmp_path / "test.db"

    repository = JobRepository(str(database_path))

    job = create_job("https://example.com/job")

    repository.save_jobs([job])
    repository.save_jobs([job])

    jobs = repository.get_all()

    assert len(jobs) == 1