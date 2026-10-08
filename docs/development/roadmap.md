# JobScope — Development Roadmap

## Purpose

This roadmap describes the planned evolution of JobScope from its current backend foundation toward a complete job discovery and analysis application.

The roadmap is intentionally progressive.

Features should be implemented when their requirements are understood and when they provide meaningful value to the product.

---

# Current Status

## Phase 0 — Backend Foundation

**Status: Completed**

The initial backend foundation is operational.

Implemented:

- FastAPI application
- Project structure
- Configuration system
- Source abstraction
- Source registry
- RemoteOK adapter
- Remotive adapter
- Arbeitnow adapter
- Job schema
- Filtering service
- Matching service
- Scoring service
- SQLite repository
- Job persistence
- URL-based deduplication
- Application logging
- Basic exception hierarchy
- Automated tests
- API endpoint for job collection

Current test suite:

```text
8 tests passed
```

---

# Phase 1 — Backend Stabilization

**Status: Next**

The next stage focuses on improving the existing backend before adding major new functionality.

Planned work:

- Review current architecture
- Improve error handling
- Review configuration validation
- Improve test coverage
- Review source adapter behavior
- Improve repository behavior
- Add tests for important edge cases
- Review API responses
- Improve documentation
- Prepare the repository for GitHub

The objective is to make the current foundation reliable before expanding the system.

---

# Phase 2 — Job Search and API Improvements

**Status: Planned**

The backend should expose more useful ways to consume stored and collected jobs.

Potential functionality:

- Retrieve persisted jobs
- Filter jobs through API parameters
- Sort jobs
- Filter by recommendation
- Filter by source
- Filter by score
- Pagination
- Job detail endpoint

The API should remain domain-agnostic.

For example, the system should not create endpoints specifically tied to one technology such as:

```text
/jobs/search/python
```

Instead, filtering and search criteria should remain configurable.

---

# Phase 3 — Improved Matching

**Status: Planned**

The current matching system uses normalized text matching.

Future improvements may include:

- Better phrase matching
- Synonym handling
- Technology aliases
- Seniority normalization
- Location normalization
- Skill extraction
- More precise matching rules

The goal is to improve relevance without immediately introducing AI.

---

# Phase 4 — Improved Scoring

**Status: Planned**

The current scoring system provides a deterministic baseline.

Future work may include:

- More granular scoring
- Explainable scoring reasons
- Configurable score components
- Experience compatibility
- Skill coverage
- Salary compatibility
- Employment type
- Source quality

A future result could provide:

```text
Score: 87

Role match:       +40
Seniority match:  +25
Location match:   +20
Keyword match:    +15

Potential concerns:
- Required experience above profile
```

The scoring system should remain understandable and testable.

---

# Phase 5 — More Job Sources

**Status: Planned**

Additional providers can be introduced through the existing source adapter architecture.

Potential future sources include:

- Adzuna
- The Muse
- Hacker News Jobs or equivalent compatible sources
- Other public job APIs
- Carefully selected scraping integrations where appropriate

Each source should remain isolated behind the source abstraction.

The main pipeline should not need to change when a new provider is added.

---

# Phase 6 — Persistent Profiles

**Status: Planned**

The current profile is configuration-based.

A future application may require profiles to become persistent domain entities.

Possible concepts:

```text
User
 │
 └── Profile
       ├── Target roles
       ├── Seniority
       ├── Locations
       ├── Skills
       ├── Keywords
       └── Preferences
```

This phase should only begin when the application actually requires multiple users or multiple persistent profiles.

---

# Phase 7 — Frontend Application

**Status: Planned**

Once the backend API is sufficiently stable, a dedicated frontend can be built.

Potential functionality:

- Dashboard
- Job search
- Job cards
- Job detail pages
- Score visualization
- Recommendation indicators
- Filters
- Saved jobs
- Profile management

The frontend should consume the backend through the public API rather than depending on internal Python services.

---

# Phase 8 — Advanced Job Analysis

**Status: Planned**

Advanced analysis can be introduced after the deterministic pipeline is stable.

Possible capabilities:

- NLP
- Semantic similarity
- Skill extraction
- Experience comparison
- Job description summarization
- Requirement analysis
- AI-assisted explanations

AI should remain an optional analysis layer rather than becoming a mandatory dependency of the entire backend.

---

# Phase 9 — Application Tracking

**Status: Future**

JobScope may eventually manage the user's application workflow.

Possible states:

```text
Saved
   ↓
Reviewing
   ↓
Applied
   ↓
Interview
   ↓
Offer
```

The system could additionally store:

- Application dates
- Notes
- Interview information
- Contacts
- Documents
- Follow-up reminders

This phase transforms JobScope from a discovery tool into a broader job-search management system.

---

# Phase 10 — Production Infrastructure

**Status: Future**

If the application reaches production scale, infrastructure requirements may expand.

Potential work:

- PostgreSQL
- Authentication
- Background jobs
- Caching
- Rate limiting
- API security
- Containerization
- Cloud deployment
- Monitoring
- Observability
- Automated deployment

These concerns are intentionally postponed until there is a real operational requirement.

---

# Long-Term Architecture

The potential long-term architecture could evolve toward:

```text
                    JOBSCOPE
                       │
             ┌─────────▼─────────┐
             │    API / Frontend │
             └─────────┬─────────┘
                       │
                 Application
                   Services
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Sources        Analysis       Profiles
        │              │              │
        ▼              ▼              ▼
     Job Data      Job Analysis    User Data
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                   Persistence
```

This is a possible direction rather than the current implementation.

---

# Development Principles

## Build in Vertical Slices

New functionality should ideally provide an end-to-end capability rather than introducing isolated infrastructure without a clear use case.

---

## Stabilize Before Expanding

Existing functionality should be tested and understood before major architectural changes are introduced.

---

## Prefer Demonstrated Requirements

A new abstraction should exist because the application needs it, not because it might theoretically be useful someday.

---

## Preserve Domain Independence

The backend should avoid becoming tightly coupled to:

- One programming language
- One job title
- One technology stack
- One job provider
- One frontend

---

## Keep the Core Testable

Business logic should remain testable without requiring external APIs or a running frontend.

---

# Current Priority

The immediate priority is:

```text
Stabilize
   ↓
Test
   ↓
Document
   ↓
Publish
   ↓
Review architecture
   ↓
Expand functionality
```

The goal is not to build every planned feature immediately.

The goal is to establish a strong backend foundation that can support the complete JobScope application as its requirements become clearer.