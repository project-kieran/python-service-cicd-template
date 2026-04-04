# Python Service CI/CD Template

A minimal starter template for Python services, intended to include testing, linting, Docker, and GitHub Actions.

## Why this exists

Starting a new service often means repeating the same setup work: project structure, test configuration, linting, containerisation, and CI. This repository is being created as a small, reusable baseline that can grow into a practical starting point for future Python services without unnecessary complexity.

## Planned contents

This repository is intended to include:

- a minimal Python service
- test setup with `pytest`
- linting and formatting
- a Dockerfile for local container builds
- a GitHub Actions workflow for CI
- a clear project structure for reuse

## Intended pipeline

Once implemented, the CI pipeline will aim to:

1. install dependencies
2. run linting and formatting checks
3. run tests
4. build the Docker image

The goal is to create a simple but practical baseline for validating code changes before deployment.

## Planned project structure

```text
.
├── .github/workflows/   # GitHub Actions workflows
├── app/                 # application code
├── tests/               # test suite
├── Dockerfile           # container build definition
├── requirements.txt     # Python dependencies
└── README.md
```

## Design goals

This template is intended to stay small and readable. The aim is to provide a clean starting point for a Python service rather than a complete production platform.

Current priorities:

- simple structure over heavy abstraction
- local-first development workflow
- CI focused on core validation only
- no cloud deployment in the initial version

## Scope

The initial version is not intended to include:

- deployment to a cloud platform
- secrets management
- release automation
- infrastructure provisioning

These may be considered later depending on the direction of the project.

## Roadmap

Planned next steps:

- create the initial folder structure
- add a small example Python service
- add test scaffolding
- add linting and formatting
- add a Dockerfile
- add a GitHub Actions workflow
- document local setup and usage

## License

MIT