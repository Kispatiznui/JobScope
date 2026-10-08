import requests

from app.schemas.job import Job
from app.sources.base import JobSource
from app.core.exceptions import SourceError


class RemotiveSource(JobSource):

    API_URL = "https://remotive.com/api/remote-jobs"

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
            f"Error obteniendo datos de Remotive: {exc}"
        ) from exc

        data = response.json()

        jobs = []

        for item in data.get("jobs", []):
            if not isinstance(item, dict):
                continue

            title = item.get("title")
            company = item.get("company_name")
            url = item.get("url")

            if not title or not company or not url:
                continue

            jobs.append(
                Job(
                    title=title,
                    company=company,
                    url=url,
                    location=item.get("candidate_required_location"),
                    description=item.get("description"),
                    salary=item.get("salary"),
                    source="remotive",
                )
            )

        return jobs