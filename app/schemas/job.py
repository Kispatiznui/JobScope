from pydantic import BaseModel, Field


class Job(BaseModel):
    title: str
    company: str
    url: str

    location: str | None = None
    description: str | None = None
    salary: str | None = None

    source: str

    score: float = Field(default=0.0, ge=0)
    recommendation: str | None = None