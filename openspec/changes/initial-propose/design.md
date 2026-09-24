# Design

## Context

This design describes the architecture and technical decisions for building the Python Sine Wave Generator PoC. See `proposal.md` for motivation and `specs/sine-generator/spec.md` for normative requirements. All source code, docstrings, inline comments, log output, and CLI parameter names (`--frequency`, `--amplitude`, `--color`, `--export`) MUST be in English.

## Goals / Non-Goals

**Goals:**
- Provide a clean `src/` layout Python package using `pyproject.toml` managed by `uv`.
- Implement CLI parsing via standard library `argparse` using English argument names (`--frequency`, `--amplitude`, `--color`, `--export`).
- Calculate sine wave data using `numpy` and plot using `matplotlib`.
- Support headless rendering (`MPLBACKEND=Agg`) for container compatibility.
- Ensure automated test coverage of CLI and generator logic using `pytest`.
- Maintain code formatting and linting standards via `ruff`.
- Ensure 100% of docstrings, type annotations, inline comments, and commit messages are in English.
- Package application into a multi-stage Docker image using `python:3.11-slim`.

**Non-Goals:**
- Building a web-based GUI or REST API endpoint (pure CLI application).
- Real-time animated streaming of sine waves.
- Support for complex signal composition (harmonics, noise injection) beyond a simple sine wave.

## Decisions

### Decision 1: Use `argparse` for CLI Parsing
- **Rationale**: `argparse` is part of Python's standard library, requiring no external dependencies, providing automatic help generation, and offering simple type validation.
- **Alternatives Considered**:
  - `Typer` / `Click`: Adds extra dependencies without significant benefit for 4 CLI arguments.

### Decision 2: Headless Matplotlib Backend (`MPLBACKEND=Agg`)
- **Rationale**: Prevents `Tcl/Tk` or `X11` errors inside headless Docker containers by forcing non-gui file rendering.
- **Alternatives Considered**:
  - Installing `python3-tk` and X server dependencies in Docker (bloats image size and introduces security surface).

### Decision 3: Project Packaging with `uv`
- **Rationale**: `uv` provides extremely fast dependency resolution, environment isolation, and adheres to PEP 517 / PEP 621 standards.
- **Alternatives Considered**:
  - `poetry`: Slower installation times in CI/Docker build steps.

### Decision 4: Multi-stage Dockerfile based on `python:3.11-slim`
- **Rationale**: Minimizes image size and ensures security by dropping unnecessary build toolchains in the runtime stage.

## Risks / Trade-offs

- [Risk] Incorrect Matplotlib backend initialization in graphical environments → Configure `matplotlib.use('Agg')` explicitly before rendering to guarantee headless behavior regardless of system settings.
- [Risk] Invalid color name provided by user → Catch `ValueError` or invalid matplotlib color specifications in `argparse` validation layer and present clear CLI user feedback in English.
