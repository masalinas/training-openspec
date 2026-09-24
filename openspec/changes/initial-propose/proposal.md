# Proposal

## Why

Establish a high-quality Python Proof of Concept (PoC) for generating sine wave plots via a command-line interface (CLI). This project sets up project scaffolding following modern Python best practices (using `pyproject.toml`, `uv`, `pytest`, `ruff`, and Docker), serving as a benchmark for robust CLI applications and reproducible container deployments. All code, comments, docstrings, and CLI interfaces must be written in English.

## What Changes

- **Project Scaffolding**: Configure `pyproject.toml` with `uv` build system, dependency declarations (`matplotlib`, `numpy`), dev tools (`pytest`, `ruff`), and `.gitignore`.
- **CLI Interface**: Implement a CLI using Python's standard library `argparse` to accept `--frequency`, `--amplitude`, `--color`, and optional `--export` PNG flag.
- **Sine Generator Engine**: Implement calculation and visualization logic using `numpy` and `matplotlib` with headless rendering support (`MPLBACKEND=Agg`).
- **Export Utility**: Generate output files named `senoide_YYYYMMDDHHmmSS.png` based on current timestamp when PNG export is requested.
- **Unit Tests & Quality**: Add unit tests with `pytest` covering calculations, CLI parsing, and file export, alongside `ruff` linting and formatting.
- **Dockerization**: Provide a multi-stage `Dockerfile` based on `python:3.11-slim` for headless execution in container environments.

## Capabilities

### New Capabilities
- `sine-generator`: Capability to generate sine wave plots via CLI arguments and export them to timestamped PNG files.

### Modified Capabilities

## Impact

- **New files**: `pyproject.toml`, `Dockerfile`, `.gitignore`, `.dockerignore`, `src/sine_generator/*`, `tests/*`.
- **Dependencies**: `matplotlib`, `numpy`, `pytest` (dev), `ruff` (dev).
