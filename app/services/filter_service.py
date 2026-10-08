from app.schemas.job import Job
from app.services.config_service import load_config


class FilterService:

    def __init__(self):
        self.config = load_config("filters.json")

        self.excluded_keywords = self.config.get(
            "excluded_keywords",
            [],
        )

        self.excluded_locations = self.config.get(
            "excluded_locations",
            [],
        )

        self.excluded_companies = self.config.get(
            "excluded_companies",
            [],
        )

        self.excluded_titles = self.config.get(
            "excluded_titles",
            [],
        )

    def is_allowed(self, job: Job) -> bool:
        if self._matches_excluded_keyword(job):
            return False

        if self._matches_excluded_location(job):
            return False

        if self._matches_excluded_company(job):
            return False

        if self._matches_excluded_title(job):
            return False

        return True

    def _matches_excluded_keyword(self, job: Job) -> bool:
        text = " ".join(
            [
                job.title or "",
                job.location or "",
                job.description or "",
            ]
        ).lower()

        return self._contains_any(
            text,
            self.excluded_keywords,
        )

    def _matches_excluded_location(self, job: Job) -> bool:
        location = (job.location or "").lower()

        return self._contains_any(
            location,
            self.excluded_locations,
        )

    def _matches_excluded_company(self, job: Job) -> bool:
        company = (job.company or "").lower()

        return self._contains_any(
            company,
            self.excluded_companies,
        )

    def _matches_excluded_title(self, job: Job) -> bool:
        title = (job.title or "").lower()

        return self._contains_any(
            title,
            self.excluded_titles,
        )

    def _contains_any(
        self,
        text: str,
        values: list[str],
    ) -> bool:
        return any(
            value.lower() in text
            for value in values
        )