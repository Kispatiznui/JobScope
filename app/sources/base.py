from abc import ABC, abstractmethod

from app.schemas.job import Job


class JobSource(ABC):

    @abstractmethod
    def fetch_jobs(self) -> list[Job]:
        pass