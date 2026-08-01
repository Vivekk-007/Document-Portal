# Use Python 3.11 slim image
FROM python:3.11-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Copy dependency files first (better Docker caching)
COPY pyproject.toml uv.lock* ./

# Install project dependencies
RUN uv sync --frozen --no-dev

# Copy the project
COPY . .

# Expose FastAPI port
EXPOSE 8080

# Run FastAPI
CMD ["uv", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "4"]