# Tasks

## 1. Project Scaffolding & Configuration

- [x] 1.1 Create `pyproject.toml` with `uv` configuration, declaring dependencies (`matplotlib`, `numpy`) and dev tools (`pytest`, `ruff`), ensuring all metadata is in English, and verify syntax.
- [x] 1.2 Create `.gitignore` and `.dockerignore` files for Python and Docker artifacts, and verify git ignores temporary build files.

## 2. Core Implementation

- [x] 2.1 Implement `src/sine_generator/utils.py` with timestamped PNG filename generator (`senoide_YYYYMMDDHHmmSS.png`), English docstrings and comments, verifying output formatting.
- [x] 2.2 Implement `src/sine_generator/generator.py` with `numpy` sine wave calculation and `matplotlib` rendering with `MPLBACKEND=Agg`, using English docstrings/comments, verifying PNG generation.
- [x] 2.3 Implement `src/sine_generator/cli.py` and `main.py` using `argparse` to accept `--frequency`, `--amplitude`, `--color`, and `--export` flags with English help strings and comments, verifying argument parsing.

## 3. Testing & Code Quality

- [x] 3.1 Write unit tests in `tests/test_utils.py` for filename timestamp formatting using English test function names and docstrings, verifying tests pass using `pytest`.
- [x] 3.2 Write unit tests in `tests/test_generator.py` for sine wave data generation and file export using English docstrings, verifying tests pass using `pytest`.
- [x] 3.3 Write CLI unit tests in `tests/test_cli.py` verifying `argparse` inputs (`--frequency`, `--amplitude`, `--color`, `--export`) and English `--help` output, verifying tests pass using `pytest`.
- [x] 3.4 Run `ruff check` and `ruff format` across `src/` and `tests/`, verifying code passes linting without errors.

## 4. Containerization & Deployment

- [x] 4.1 Create multi-stage `Dockerfile` based on `python:3.11-slim` with `uv` for dependency installation with English comments, verifying `docker build` succeeds.
- [x] 4.2 Verify containerized execution by running the Docker image with CLI parameters (`--frequency`, `--amplitude`, `--color`, `--export`) and verifying PNG export output inside container mount.
