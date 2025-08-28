# Use a slim Python base image
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONIOENCODING=UTF-8

WORKDIR /app

# Set Python path to include the current directory
ENV PYTHONPATH=/app:$PYTHONPATH

# Install system dependencies if needed (uncomment if wheels fail)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#  && rm -rf /var/lib/apt/lists/*

# Copy requirement files first for better caching
COPY requirements.txt ./
COPY requirements-mcp.txt ./

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install -r requirements-mcp.txt

# Copy the rest of the source code
COPY . .

# Copy production environment file (create from .env.prod.example if needed)
COPY .env.prod* ./
RUN if [ -f .env.prod ]; then cp .env.prod .env; else echo "Warning: .env.prod not found, using defaults"; fi

# Create logs directory
RUN mkdir -p logs

# Default Flask port from settings/local.py
EXPOSE 9000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:9000/health || exit 1

# Run with Waitress in production
# Use environment variables for configuration
CMD ["sh", "-c", "waitress-serve --host=0.0.0.0 --port=${PORT:-9000} --threads=${WAITRESS_THREADS:-8} wsgi:application"]



