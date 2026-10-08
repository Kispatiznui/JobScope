from app.schemas.job import Job
from app.services.config_service import load_profile
import re

class MatchingService:

    def __init__(self):
        self.profile = load_profile()

    def matches(self, job: Job) -> bool:
        text = self._build_search_text(job)

        role_match = self._matches_any(
            text,
            self.profile.get("target_roles", []),
        )

        seniority_match = self._matches_any(
            text,
            self.profile.get("target_seniority", []),
        )

        location_match = self._matches_any(
            text,
            self.profile.get("preferred_locations", []),
        )

        return role_match and seniority_match and location_match

    def _build_search_text(self, job: Job) -> str:
        return " ".join(
            [
                job.title or "",
                job.location or "",
                job.description or "",
            ]
        ).lower()

    def _matches_any(
        self,
        text: str,
        values: list[str],
        ) -> bool:
        normalized_text = self._normalize(text)

        return any(
        self._normalize(value) in normalized_text
        for value in values
    )
    def _normalize(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^a-z0-9áéíóúüñ\s]", " ", text)
        return " ".join(text.split())