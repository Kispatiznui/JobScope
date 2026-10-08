import sqlite3

from app.schemas.job import Job


class JobRepository:

    def __init__(self, database_path: str = "data/jobscope.db"):
        self.database_path = database_path
        self._create_table()

    def _create_table(self):
        connection = sqlite3.connect(self.database_path)

        try:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    company TEXT NOT NULL,
                    url TEXT NOT NULL UNIQUE,
                    location TEXT,
                    description TEXT,
                    salary TEXT,
                    source TEXT NOT NULL,
                    score REAL NOT NULL,
                    recommendation TEXT
                )
                """
            )

            connection.commit()

        finally:
            connection.close()

    def save_jobs(self, jobs: list[Job]):
        connection = sqlite3.connect(self.database_path)

        try:
            for job in jobs:
                connection.execute(
                    """
                    INSERT OR REPLACE INTO jobs (
                        title,
                        company,
                        url,
                        location,
                        description,
                        salary,
                        source,
                        score,
                        recommendation
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        job.title,
                        job.company,
                        job.url,
                        job.location,
                        job.description,
                        job.salary,
                        job.source,
                        job.score,
                        job.recommendation,
                    ),
                )

            connection.commit()

        finally:
            connection.close()

    def get_all(self) -> list[Job]:
        connection = sqlite3.connect(self.database_path)

        try:
            rows = connection.execute(
                """
                SELECT
                    title,
                    company,
                    url,
                    location,
                    description,
                    salary,
                    source,
                    score,
                    recommendation
                FROM jobs
                ORDER BY score DESC
                """
            ).fetchall()

            return [
                Job(
                    title=row[0],
                    company=row[1],
                    url=row[2],
                    location=row[3],
                    description=row[4],
                    salary=row[5],
                    source=row[6],
                    score=row[7],
                    recommendation=row[8],
                )
                for row in rows
            ]

        finally:
            connection.close()