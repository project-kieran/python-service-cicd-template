# Python Service CI/CD Template

A minimal starter template for Python services with FastAPI, pytest, Docker, and GitHub Actions.

## Why this exists

Starting a new service often means repeating the same setup work: project structure, test configuration, containerisation, and CI. This repository provides a small, reusable baseline for Python services without unnecessary complexity.

## What’s included

* a minimal FastAPI service
* endpoint tests with `pytest`
* Dockerfile for local container builds
* GitHub Actions workflow for continuous integration
* simple project structure for reuse and extension

## Project structure

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

## Quick start

### Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application locally

```bash
uvicorn app.main:app --reload
```

### Run tests

```bash
python -m pytest
```

## API endpoints

The example service currently includes:

* `GET /` – welcome message
* `GET /health` – basic health check
* `GET /version` – example version response
* `GET /time` – current server time

## Docker

Build the image:

```bash
docker build -t python-service-cicd-template .
```

Run the container:

```bash
docker run -p 8000:8000 python-service-cicd-template
```

## CI workflow

The GitHub Actions workflow runs on push and pull request. It currently:

1. checks out the repository
2. sets up Python
3. installs dependencies
4. runs the test suite

## Design goals

This template is intentionally small and readable. The aim is to provide a clean starting point for a Python service rather than a complete production platform.

Current priorities:

* simple structure over heavy abstraction
* local-first development workflow
* CI focused on core validation
* a baseline that can be extended later

## Scope

This repository does not currently include:

* cloud deployment
* secrets management
* release automation
* infrastructure provisioning
* linting and formatting checks in CI

These can be added later depending on the direction of the project.

## Roadmap

Possible next steps:

* add linting and formatting
* extend the CI workflow to include quality checks
* add Docker image validation in CI
* add environment-based configuration
* document production considerations
