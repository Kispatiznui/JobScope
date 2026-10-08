from app.schemas.job import Job
from app.services.config_service import load_config


class ScoringService:

    def __init__(self):
        self.config = load_config("scoring.json")
        self.profile = load_config("profile.json")
        self.keywords_config = load_config("keywords.json")

        self.weights = self.config["weights"]
        self.thresholds = self.config["thresholds"]
        self.keywords = self.keywords_config.get("keywords", [])

    def score(self, job: Job) -> Job:
        text = self._build_search_text(job)

        score = 0.0

        if self._contains_any(
            text,
            self.profile.get("target_roles", []),
        ):
            score += self.weights["role"]

        if self._contains_any(
            text,
            self.profile.get("target_seniority", []),
        ):
            score += self.weights["seniority"]

        if self._contains_any(
            text,
            self.profile.get("preferred_locations", []),
        ):
            score += self.weights["location"]

        if self._contains_any(text, self.keywords):
            score += self.weights["keywords"]

        recommendation = self._get_recommendation(score)

        return job.model_copy(
            update={
                "score": score,
                "recommendation": recommendation,
            }
        )

    def _build_search_text(self, job: Job) -> str:
        return " ".join(
            [
                job.title or "",
                job.location or "",
                job.description or "",
            ]
        ).lower()

    def _contains_any(
        self,
        text: str,
        values: list[str],
    ) -> bool:
        return any(
            value.lower() in text
            for value in values
        )

    def _get_recommendation(self, score: float) -> str:
        if score >= self.thresholds["high"]:
            return "high"

        if score >= self.thresholds["medium"]:
            return "medium"

        return "low"