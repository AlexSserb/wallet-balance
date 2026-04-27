# Stage 1: install dependencies into an isolated venv
FROM python:3.13-slim AS builder

WORKDIR /build

# uv is a fast Python package installer written in Rust
RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

# UV_PROJECT_ENVIRONMENT sets the venv path used in both stages
ENV UV_PROJECT_ENVIRONMENT="/opt/venv"

# --frozen: fail if uv.lock is out of sync with pyproject.toml
# --no-dev: exclude pytest, ruff, ty from the production image
RUN uv sync --frozen --no-dev

# Stage 2: minimal runtime image without build tools
FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
# Send Python output straight to stdout without buffering
ENV PYTHONUNBUFFERED=1

COPY . .

EXPOSE 8000

# 4 worker processes; each maintains its own SQLAlchemy connection pool
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]