# JobScope — Architecture Decisions

This document records the main architectural decisions made during the development of JobScope.

The purpose is not to document every implementation detail, but to preserve the reasoning behind decisions that affect the structure and evolution of the backend.

---

## ADR-001 — Use FastAPI

### Decision

JobScope uses FastAPI as its HTTP framework.

### Reasoning

FastAPI provides:

- Type-safe request and response definitions through Pydantic
- Automatic OpenAPI documentation
- Good support for modular application structures
- A clear separation between API routes and application services

It also provides a practical foundation for a future frontend or external client.

### Consequence

The API layer remains relatively thin while business logic stays inside services.

---

## ADR-002 — Use Source Adapters

### Decision

Each external job provider is implemented through a dedicated source adapter.

Current adapters include:

```text
RemoteOKSource
RemotiveSource
ArbeitnowSource
```

### Reasoning

External APIs have different response formats and behaviors.

The rest of JobScope should not need to know those differences.

Each adapter is responsible for:

1. Calling its external provider.
2. Handling provider-specific responses.
3. Converting the response into the common `Job` schema.

### Consequence

Adding another job provider should not require changes to filtering, matching, scoring or persistence.

---

## ADR-003 — Use a Source Registry

### Decision

Available source adapters are registered in:

```text
app/sources/registry.py
```

### Reasoning

The job pipeline should not contain hardcoded source instantiation logic.

The registry provides a single place where available providers are declared.

### Consequence

The source configuration can determine which registered providers are enabled.

---

## ADR-004 — Use JSON Configuration

### Decision

User preferences and operational settings are stored in JSON files.

Current configuration includes:

```text
config/
├── profile.json
├── keywords.json
├── scoring.json
├── sources.json
└── filters.json
```

### Reasoning

The backend should be configurable without requiring changes to Python source code.

This is particularly important because JobScope is intended to remain domain-agnostic.

### Consequence

The same core application can operate with different profiles, keywords, filters, scoring weights and enabled sources.

---

## ADR-005 — Do Not Create a Separate Normalizer Layer

### Decision

JobScope does not currently implement a separate normalization service.

### Reasoning

Each source adapter already converts provider-specific data into the shared `Job` schema.

Adding another normalization layer would introduce an additional abstraction without solving a demonstrated problem.

### Consequence

Normalization remains close to the external-source boundary.

If normalization becomes significantly more complex in the future, the architecture can be reconsidered.

---

## ADR-006 — Keep Matching and Scoring Separate

### Decision

Matching and scoring remain separate services.

### Reasoning

They answer different questions.

Matching asks:

> Does this job satisfy the current profile criteria?

Scoring asks:

> How strongly does this job match the configured criteria?

Keeping them separate makes their behavior easier to reason about and test.

### Consequence

Future matching techniques such as NLP or semantic similarity can evolve without necessarily replacing the scoring mechanism.

---

## ADR-007 — Avoid Premature AI Integration

### Decision

The current backend does not depend on an external AI provider.

### Reasoning

The deterministic pipeline provides a working baseline that can be tested and understood.

Introducing AI before establishing this baseline would make behavior harder to debug and introduce:

- External API dependencies
- Cost
- Credentials management
- Latency
- Additional failure modes

### Consequence

AI or NLP can be introduced later as an additional analysis capability rather than becoming a mandatory dependency of the core pipeline.

---

## ADR-008 — Use SQLite for the Current Persistence Layer

### Decision

SQLite is used for the current repository implementation.

### Reasoning

The current project is a backend MVP and does not yet require the operational complexity of a production database server.

SQLite provides:

- Persistence
- SQL querying
- Transaction support
- Minimal infrastructure
- Easy local development

### Consequence

The repository abstraction allows the persistence implementation to evolve later.

A future version may use PostgreSQL or another database without requiring the rest of the application to know the database implementation details.

---

## ADR-009 — Use URL Uniqueness for Initial Deduplication

### Decision

The job URL is currently unique in the SQLite database.

### Reasoning

The URL provides a simple and practical identity for the current source data.

### Consequence

Repeated ingestion of the same URL does not create multiple records.

However, this is not considered a complete semantic deduplication strategy.

Different URLs may still represent the same underlying job.

A more advanced deduplication mechanism may be introduced later if required.

---

## ADR-010 — Keep Business Logic Outside API Routes

### Decision

FastAPI routes should delegate processing to services rather than implementing business logic directly.

### Reasoning

The backend may eventually be consumed by:

- A web frontend
- A mobile application
- CLI tools
- Automated processes
- Other services

Business logic should therefore remain independent of HTTP.

### Consequence

API routes remain thin and the core behavior can be reused by other interfaces.

---

## ADR-011 — Use Automated Tests Before Major Expansion

### Decision

Core services and persistence behavior should have automated tests before significant architectural expansion.

### Current Coverage

The current test suite covers:

```text
MatchingService
FilterService
ScoringService
JobRepository
```

Current result:

```text
8 tests passed
```

### Reasoning

Tests provide a safety net for future refactoring.

They also establish expected behavior before introducing more advanced functionality.

---

## ADR-012 — Avoid Premature Domain Modeling

### Decision

Future concepts such as users, profiles, saved jobs and applications are not implemented yet.

### Reasoning

The current backend does not require them to perform its core function.

Implementing them prematurely would increase complexity without providing immediate value.

### Consequence

The current model remains small.

As the complete application is designed, these concepts can be introduced when their requirements are understood.

---

## Architectural Philosophy

The general philosophy behind JobScope is:

> Build the smallest architecture that establishes strong boundaries and can evolve without a rewrite.

This means:

- Prefer clear responsibilities over excessive abstraction.
- Prefer configuration over hardcoding.
- Isolate external dependencies.
- Keep business logic independent from HTTP.
- Test important behavior.
- Introduce new layers only when a real problem requires them.

The architecture is intentionally incomplete because the complete application has not yet been designed.

The backend is being built as a foundation rather than as a prematurely finalized product.
