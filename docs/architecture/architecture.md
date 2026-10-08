# JobScope — Architecture

## Architectural Structure

JobScope is organized around a small set of responsibilities:

```text
app/
│
├── api/
│   └── HTTP interface
│
├── core/
│   └── application-level infrastructure
│
├── models/
│   └── domain models
│
├── repositories/
│   └── persistence
│
├── schemas/
│   └── data contracts
│
├── services/
│   └── business logic
│
└── sources/
    └── external job providers

    The architecture intentionally avoids unnecessary layers and abstractions.
Layers
API
Location:
app/api/

The API layer exposes JobScope through HTTP.
Routes are responsible for:
- Receiving HTTP requests
- Calling application services
- Returning serialized responses
Routes should not contain the main business logic.
Current routes include:
app/api/routes/jobs.py

Core
Location:
app/core/

The core package contains functionality shared across the application.
Current components include:
config.py
exceptions.py
logging.py

Configuration
config.py provides centralized access to configuration paths.
Exceptions
exceptions.py defines application-level exceptions such as:
JobScopeException
SourceError
ConfigurationError

Logging
logging.py provides the application's logging configuration.
Schemas
Location:
app/schemas/

Schemas define the data contracts used by the application.
The main schema is:
Job

The Job schema represents a normalized job opportunity regardless of which external source provided it.
This allows the rest of the application to work with a common structure.
Models
Location:
app/models/

This package is reserved for domain models that may become necessary as the application grows.
The current architecture keeps the main API data contract in schemas.
This separation leaves room for richer domain modeling without coupling the HTTP layer to persistence or external APIs.
Sources
Location:
app/sources/

The sources layer isolates external job providers from the rest of the application.
The main abstraction is:
JobSource

Each source implements the same basic operation:
fetch_jobs()

Current adapters:
app/sources/adapters/
├── arbeitnow.py
├── remoteok.py
└── remotive.py

The registry:
app/sources/registry.py

maps source names to their adapter classes.
This allows sources to be enabled or disabled through configuration without changing the main job pipeline.
Services
Location:
app/services/

Services contain the application's business logic.
Current services include:
config_service.py
filter_service.py
job_service.py
matching_service.py
scoring_service.py

ConfigService
Loads configuration from the config/ directory.
FilterService
Applies configurable exclusion rules.
MatchingService
Determines whether a job matches the configured profile.
ScoringService
Calculates the compatibility score and recommendation level.
JobService
Coordinates the main job-processing pipeline.
The current pipeline is:
Sources
   │
   ▼
Collect jobs
   │
   ▼
Filter
   │
   ▼
Score
   │
   ▼
Sort
   │
   ▼
Persist

Repositories
Location:
app/repositories/

Repositories isolate persistence from business logic.
Current repository:
job_repository.py

The JobRepository handles:
- Creating the jobs table
- Saving jobs
- Retrieving jobs
- Enforcing unique job URLs
The rest of the application does not need to know how SQLite is implemented.
Source Independence
One of the main architectural goals is to keep external sources independent from the rest of JobScope.
A source adapter converts external data into the common Job schema.
Conceptually:
RemoteOK API
     │
     ▼
RemoteOKSource
     │
     ▼
     Job
     │
     ▼
JobScope pipeline

The same pattern applies to other providers.
This means adding a new source should primarily require:
1. Creating a new adapter.
2. Registering it.
3. Adding its configuration.
The filtering, matching, scoring and persistence layers should not need to know where the job originated.
Configuration Independence
Important application behavior is externalized into JSON configuration files.
config/
├── profile.json
├── keywords.json
├── scoring.json
├── sources.json
└── filters.json

This prevents user-specific preferences and operational settings from becoming hardcoded into business logic.
The goal is to keep the backend domain-agnostic.
Dependency Direction
The intended dependency direction is:
API
 │
 ▼
Services
 │
 ├──────────────► Sources
 │
 ├──────────────► Repositories
 │
 └──────────────► Configuration

Schemas provide shared data contracts used by these components.
External APIs should not directly control internal application behavior.
Architectural Principles
JobScope currently follows these principles:
1. Separation of responsibilities
Each component should have one clear reason to change.
2. Configuration over hardcoding
User preferences and operational settings belong in configuration whenever practical.
3. External-source isolation
External APIs should remain behind source adapters.
4. Business logic outside the API layer
FastAPI routes should remain thin.
5. Persistence isolation
Database implementation should remain behind repositories.
6. Avoid premature abstraction
New layers or abstractions should only be introduced when they solve a demonstrated problem.
7. Domain independence
The core should not be designed around a single programming language, job title or technology stack.
8. Future extensibility
The architecture should allow future capabilities such as:
- More job sources
- More advanced matching
- NLP
- AI-assisted analysis
- Multiple profiles
- Authentication
- Alternative databases
- A dedicated frontend
without requiring a complete rewrite of the current core.