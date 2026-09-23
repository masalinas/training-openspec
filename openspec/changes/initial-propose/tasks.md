# Tasks

## 1. Project Scaffolding & Configuration

- [ ] 1.1 Create `pyproject.toml` with `uv` configuration, declaring dependencies (`matplotlib`, `numpy`) and dev tools (`pytest`, `ruff`), and verify syntax.
- [ ] 1.2 Create `.gitignore` and `.dockerignore` files for Python and Docker artifacts, and verify git ignores temporary build files.

## 2. Core Implementation

- [ ] 2.1 Implement `src/sine_generator/utils.py` with timestamped PNG filename generator (`senoide_YYYYMMDDHHmmSS.png`) and verify output formatting.
- [ ] 2.2 Implement `src/sine_generator/generator.py` with `numpy` sine wave calculation and `matplotlib` rendering with `MPLBACKEND=Agg`, verifying PNG generation.
- [ ] 2.3 Implement `src/sine_generator/cli.py` and `main.py` using `argparse` to accept frequency, amplitude, color, and export flags, verifying argument parsing.

## 3. Testing & Code Quality

- [ ] 3.1 Write unit tests in `tests/test_utils.py` for filename timestamp formatting and verify tests pass using `pytest`.
- [ ] 3.2 Write unit tests in `tests/test_generator.py` for sine wave data generation and file export, verifying tests pass using `pytest`.
- [ ] 3.3 Write CLI unit tests in `tests/test_cli.py` verifying `argparse` inputs and `--help` flag, verifying tests pass using `pytest`.
- [ ] 3.4 Run `ruff check` and `ruff format` across `src/` and `tests/`, verifying code passes linting without errors.

## 4. Containerization & Deployment

- [ ] 4.1 Create multi-stage `Dockerfile` based on `python:3.11-slim` with `uv` for dependency installation, verifying `docker build` succeeds.
- [ ] 4.2 Verify containerized execution by running the Docker image with CLI parameters and verifying PNG export output inside container mount.
