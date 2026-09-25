# Multi-stage Dockerfile for Sine Generator CLI application using python:3.11-slim and uv

# --- Stage 1: Build stage ---
FROM python:3.11-slim AS builder

# Install uv package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency definition files first for optimal layer caching
COPY pyproject.toml README.md /app/

# Install dependencies into virtual environment using uv
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev --no-install-project

# Copy source code and install project package
COPY src/ /app/src/
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev

# --- Stage 2: Final runtime stage ---
FROM python:3.11-slim AS runner

# Set environment variables for Python and Matplotlib headless backend
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    MPLBACKEND=Agg \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Create non-root user for security best practices
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

# Copy installed virtual environment and source files from builder stage
COPY --from=builder --chown=appuser:appuser /app /app

# Switch to non-root user
USER appuser

# Set entrypoint to run the sine-generator CLI command
ENTRYPOINT ["sine-generator"]
CMD ["--help"]
