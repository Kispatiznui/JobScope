import logging

from app.schemas.job import Job
from app.services.config_service import load_sources
from app.services.filter_service import FilterService
from app.services.scoring_service import ScoringService
from app.sources.registry import SOURCE_REGISTRY
from app.core.exceptions import SourceError
from app.repositories.job_repository import JobRepository

logger = logging.getLogger(__name__)


class JobService:

    def __init__(self):
        self.source_config = load_sources()
        self.sources = self._load_enabled_sources()
        self.filter_service = FilterService()
        self.scorer = ScoringService()
        self.repository = JobRepository()

    def _load_enabled_sources(self):
        sources = []

        for source_name, source_class in SOURCE_REGISTRY.items():
            config = self.source_config["sources"].get(source_name, {})

            if config.get("enabled", False):
                sources.append(source_class())

        return sources

    def get_jobs(self) -> list[Job]:
        jobs = []

        for source in self.sources:
            try:
                source_jobs = source.fetch_jobs()
                jobs.extend(source_jobs)

                logger.info(
                    "Fuente %s: %s empleos obtenidos",
                    source.__class__.__name__,
                    len(source_jobs),
                )

            except SourceError as exc:
                logger.error(
                    "Error en fuente %s: %s",
                    source.__class__.__name__,
                    exc,
                )

        filtered_jobs = [
            job
            for job in jobs
            if self.filter_service.is_allowed(job)
        ]

        scored_jobs = [
            self.scorer.score(job)
            for job in filtered_jobs
        ]

        scored_jobs.sort(
            key=lambda job: job.score,
            reverse=True,
        )
        self.repository.save_jobs(scored_jobs)
        return scored_jobs