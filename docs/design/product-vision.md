# JobScope — Product Vision

## Vision

JobScope aims to become a configurable job discovery and analysis platform that helps users identify opportunities that are relevant to their skills, preferences and career goals.

The current backend is the foundation of that system.

The project is intentionally being developed from the backend outward, establishing reliable job collection, filtering, matching, scoring and persistence before building the complete user-facing application.

---

# Problem

Searching for jobs across multiple platforms can become repetitive and inefficient.

Users may need to:

- Search several job boards independently.
- Repeatedly evaluate whether a position fits their profile.
- Compare opportunities using different criteria.
- Ignore irrelevant positions manually.
- Track opportunities across different sources.
- Determine which opportunities deserve attention first.

JobScope is intended to reduce this friction by centralizing job collection and applying configurable analysis.

---

# Product Concept

The central idea is:

> JobScope should not simply collect jobs. It should help determine which jobs are worth the user's attention.

The system therefore separates job collection from job analysis.

Conceptually:

```text
External Job Sources
        │
        ▼
   Job Collection
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
     Analysis
        │
        ▼
   User Decisions
```

The final decision should remain with the user.

JobScope provides information and prioritization rather than automatically deciding which opportunities the user must pursue.

---

# Target Experience

A future JobScope application should allow a user to define a profile containing information such as:

- Target roles
- Seniority
- Preferred locations
- Technologies
- Exclusions
- Other job preferences

The system can then collect opportunities from configured sources and analyze them against that profile.

A future interface could present results such as:

```text
Backend Developer
Company A
Remote

Score: 91
Recommendation: High
```

while also explaining why the opportunity received that result.

The goal is not only to provide a score, but eventually to provide useful context around that score.

---

# Configurability

JobScope should remain configurable rather than being designed exclusively around one user's profile.

The backend should therefore avoid assumptions such as:

```text
Python developer
Junior
Remote
```

being permanent system rules.

These are configuration values.

The same architecture should be capable of supporting different profiles and career goals.

---

# Multi-Source Strategy

JobScope is intended to aggregate opportunities from multiple external providers.

The source architecture should allow providers to be:

- Added
- Removed
- Enabled
- Disabled
- Replaced

without requiring changes to the core analysis pipeline.

The user should ultimately be able to decide which sources are relevant to their workflow.

---

# Analysis Evolution

The current analysis is deterministic and configuration-driven.

Future versions may incorporate more advanced techniques such as:

- Improved text matching
- NLP
- Semantic similarity
- Skill extraction
- Experience analysis
- Salary analysis
- Duplicate detection
- AI-assisted job interpretation

These capabilities should enhance the existing pipeline rather than make the core system dependent on AI.

---

# Future User Features

The complete application may eventually support:

### Profiles

Users could maintain multiple career profiles.

For example:

```text
Backend Developer
Data Engineer
Cloud Developer
```

Each profile could have independent preferences and scoring behavior.

---

### Saved Jobs

Users could save interesting opportunities for later review.

Possible states could include:

```text
Saved
Reviewing
Applied
Interview
Rejected
Accepted
```

These states are future concepts and are not currently implemented.

---

### Job Analysis

A future job analysis could explain:

```text
Score: 87

Strong matches:
- Python
- FastAPI
- REST APIs
- Remote

Potential concerns:
- Requires 3+ years of experience
- English level not specified
```

This would make the system more useful than a simple numerical ranking.

---

### Application Tracking

JobScope could eventually evolve beyond job discovery into a lightweight application tracker.

The user could track:

```text
Job
 │
 └── Application
       ├── Status
       ├── Date
       ├── Notes
       └── Interview history
```

This is outside the current backend scope.

---

# Product Principles

## 1. Relevance over volume

The goal is not to collect the largest possible number of jobs.

The goal is to surface useful opportunities.

---

## 2. User control

Users should be able to configure how opportunities are evaluated.

---

## 3. Explainability

A recommendation should eventually be understandable rather than being an unexplained number.

---

## 4. Source independence

No individual job provider should define the internal architecture of JobScope.

---

## 5. Progressive intelligence

The system should evolve from deterministic rules toward more advanced analysis only when those capabilities provide real value.

---

## 6. Practicality

The product should solve real workflow problems before adding technically impressive but unnecessary features.

---

# Current Product Scope

The current version focuses on the backend foundation:

```text
Source adapters
      ↓
Job collection
      ↓
Filtering
      ↓
Matching
      ↓
Scoring
      ↓
Persistence
      ↓
FastAPI
```

The following are intentionally outside the current scope:

- Authentication
- User accounts
- Frontend
- Application tracking
- AI analysis
- Production deployment
- Multi-tenant infrastructure

These may become future capabilities as the product requirements become clearer.

---

# Long-Term Direction

JobScope could evolve from a job aggregation backend into a broader career opportunity platform.

Possible progression:

```text
Stage 1
Job collection
      ↓
Stage 2
Filtering and scoring
      ↓
Stage 3
Personalized profiles
      ↓
Stage 4
Advanced job analysis
      ↓
Stage 5
Application tracking
      ↓
Stage 6
Intelligent career assistance
```

The architecture should evolve with these requirements rather than implementing all of them in advance.

---

# Product Definition

At its core:

> JobScope is a configurable backend for transforming fragmented job listings into structured, filtered and prioritized opportunities.

The current implementation establishes the foundation for that vision without prematurely implementing the entire product.