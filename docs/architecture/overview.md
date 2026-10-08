# JobScope — Architecture Overview

## What is JobScope?

JobScope is a configurable backend for collecting, filtering, matching, scoring and persisting job opportunities from multiple sources.

The backend is designed to act as the core of a future job-search and job-analysis application.

The current version focuses on establishing a clean and extensible backend foundation rather than implementing the complete user-facing application.

---

## Core Pipeline

```text
Job Sources
     │
     ▼
Source Adapters
     │
     ▼
Normalized Job
     │
     ▼
Filtering
     │
     ▼
Matching
     │
     ▼
Scoring
     │
     ▼
Persistence
     │
     ▼
FastAPI
     │
     ▼
Future Application

Main Responsibilities
Sources
JobScope retrieves job opportunities from external job boards through source-specific adapters.
Current sources include:
- RemoteOK
- Remotive
- Arbeitnow
Sources can be enabled or disabled through configuration.
Filtering
The filtering layer removes jobs according to configurable exclusion rules.
Filters can currently target:
- Keywords
- Locations
- Companies
- Titles
Filtering happens before scoring.
Matching
The matching layer determines whether a job is compatible with the configured profile.
The current matching process considers:
- Target roles
- Target seniority
- Preferred locations
Text is normalized before matching to improve consistency.
Scoring
The scoring layer assigns a compatibility score to each job.
The current score is based on configurable weights for:
- Role
- Seniority
- Location
- Keywords
The score is also mapped to a recommendation level:
- high
- medium
- low
Persistence
JobScope currently uses SQLite for persistence.
Jobs are stored with a unique URL constraint to prevent duplicate job records.
API
FastAPI exposes the backend functionality through HTTP endpoints.
The API is intentionally kept separate from the internal services so that a future frontend or other client can consume the backend without depending on its internal implementation.
Configuration
JobScope keeps important behavior outside the application code.
Current configuration files include:
config/
├── profile.json
├── keywords.json
├── scoring.json
├── sources.json
└── filters.json

This allows the system to change its target profile, keywords, scoring behavior, filters and enabled sources without modifying the core services.
Current Architectural Principle
JobScope follows a simple principle:
Keep the core domain logic independent from external job sources and future presentation layers.

External sources are accessed through adapters.
Business logic lives in services.
Persistence is handled by repositories.
The HTTP API exposes the backend without becoming responsible for the internal business logic.
Current Scope
The current backend provides the foundation for:
- Multi-source job collection
- Job normalization
- Configurable filtering
- Profile-based matching
- Configurable scoring
- Job persistence
- Basic deduplication
- Automated tests
- HTTP API access
The complete user-facing application is intentionally outside the current scope.
Future functionality such as advanced NLP, AI-assisted analysis, richer profiles, authentication, frontend interfaces and additional infrastructure can be built on top of this backend.