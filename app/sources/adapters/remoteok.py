import requests

from app.schemas.job import Job
from app.sources.base import JobSource
from app.core.exceptions import SourceError


class RemoteOKSource(JobSource):

    API_URL = "https://remoteok.com/api"

    def fetch_jobs(self) -> list[Job]:
        try:
            response = requests.get(
            self.API_URL,
            headers={
            "User-Agent": "JobScope/0.1"
            },
             timeout=15,
        )

            response.raise_for_status()

        except requests.RequestException as exc:
            raise SourceError(
            f"Error obteniendo datos de RemoteOK: {exc}"
        ) from exc

        data = response.json()

        jobs = []

        for item in data:
            if not isinstance(item, dict):
                continue

            if not item.get("position"):
                continue

            jobs.append(
                Job(
                    title=item.get("position", ""),
                    company=item.get("company", "Unknown"),
                    url=item.get("url", ""),
                    location=item.get("location"),
                    description=item.get("description"),
                    salary=None,
                    source="remoteok",
                )
            )

        return jobs