# JobScope — Data Model

## Purpose

This document describes the data structures currently used by JobScope.

The current model is intentionally simple. It provides enough structure for collecting, analyzing and persisting job opportunities while leaving room for a richer domain model in the future.

---

# Job

The central data structure is the `Job` schema.

Location:

```text
app/schemas/job.py
```

Current structure:

```text
Job
├── title
├── company
├── url
├── location
├── description
├── salary
├── source
├── score
└── recommendation
```

### Fields

| Field | Type | Required | Purpose |
|---|---|---:|---|
| `title` | `str` | Yes | Job title |
| `company` | `str` | Yes | Company offering the position |
| `url` | `str` | Yes | Original job URL |
| `location` | `str \| None` | No | Job location |
| `description` | `str \| None` | No | Job description |
| `salary` | `str \| None` | No | Salary information when available |
| `source` | `str` | Yes | External source that provided the job |
| `score` | `float` | Yes | Current compatibility score |
| `recommendation` | `str \| None` | No | Current recommendation level |

---

# Job Identity

The current persistence layer uses the job URL as the unique identifier for deduplication.

SQLite enforces:

```text
url UNIQUE
```

Therefore, the same URL cannot create multiple job records in the current repository.

Conceptually:

```text
External Job
     │
     ▼
    URL
     │
     ▼
Unique Job Record
```

This is intentionally simple for the current stage.

A future implementation may require a more explicit job identity strategy if different sources expose equivalent jobs using different URLs.

---

# Job Source

The `source` field identifies where the job originated.

Current sources include:

```text
remoteok
remotive
arbeitnow
```

The source name is useful for:

- Identifying the origin of a job
- Debugging source-specific problems
- Filtering by source in the future
- Displaying the origin in a frontend
- Measuring source quality in the future

The source itself is not responsible for the rest of the application's processing.

---

# Profile Configuration

The current profile is stored in:

```text
config/profile.json
```

Current profile concepts include:

```text
Profile
├── name
├── target_roles
├── target_seniority
└── preferred_locations
```

Example:

```json
{
  "name": "default",
  "target_roles": [
    "backend developer",
    "python developer",
    "software engineer"
  ],
  "target_seniority": [
    "junior",
    "entry level"
  ],
  "preferred_locations": [
    "remote",
    "colombia"
  ]
}
```

At the current stage, the profile is configuration rather than a persisted database entity.

---

# Keywords

Keywords are stored separately:

```text
config/keywords.json
```

They represent technologies or terms that can contribute to job scoring.

Examples include:

```text
python
fastapi
django
javascript
typescript
rest api
sql
mongodb
docker
aws
git
```

Keywords are intentionally separated from the job model.

This allows the same job data to be analyzed using different keyword configurations.

---

# Filtering Configuration

Filtering rules are stored in:

```text
config/filters.json
```

Current categories include:

```text
excluded_keywords
excluded_locations
excluded_companies
excluded_titles
```

These values determine whether a job should remain in the processing pipeline.

Filtering does not modify the original job data.

---

# Scoring Configuration

Scoring behavior is stored in:

```text
config/scoring.json
```

The current scoring model contains:

```text
weights
├── role
├── seniority
├── location
└── keywords
```

and recommendation thresholds:

```text
thresholds
├── high
├── medium
└── low
```

The current model is deterministic and configuration-driven.

---

# Analysis vs Job Data

The current `Job` schema contains both job information and analysis information:

```text
Job
│
├── Job data
│   ├── title
│   ├── company
│   ├── url
│   ├── location
│   ├── description
│   ├── salary
│   └── source
│
└── Analysis
    ├── score
    └── recommendation
```

This is acceptable for the current MVP.

However, this distinction is important for future development.

A job itself is independent of the user analyzing it.

For example:

```text
Job A
   │
   ├── Profile A → score 87
   ├── Profile B → score 54
   └── Profile C → score 91
```

This suggests that, as JobScope evolves toward multiple users or multiple profiles, analysis may need to become a separate concept.

For example:

```text
Job
  │
  └── Analysis
        ├── profile
        ├── score
        ├── recommendation
        └── reasons
```

This is a **future design direction**, not part of the current implementation.

---

# Future Domain Evolution

The current model leaves room for additional entities such as:

```text
User
Profile
Job
JobAnalysis
Source
SavedJob
Application
```

A possible future relationship could be:

```text
User
 │
 └── Profile
       │
       └──────────────┐
                      ▼
                     Job
                      │
                      ▼
                 JobAnalysis
```

However, these entities should only be introduced when the application actually requires them.

The current backend deliberately avoids implementing them prematurely.

---

# Design Principles

The data model currently follows these principles:

### Stable job representation

External job providers are converted into a common `Job` structure.

### Configuration outside the job

Profile preferences, keywords, filters and scoring rules are not embedded into individual jobs.

### Simple identity

The job URL is currently used for deduplication.

### Analysis can evolve independently

The current score and recommendation are part of `Job` for simplicity, but the architecture recognizes that analysis may become a separate domain concept.

### Avoid premature modeling

Future entities should only become database models when there is a real requirement for them.
