#!/bin/bash

# Production startup script for CapCut API

set -e

echo "Starting CapCut API in production mode..."

# Load environment variables if .env exists
if [ -f .env ]; then
    echo "Loading environment variables from .env"
    export $(cat .env | grep -v '^#' | xargs)
fi

# Set default values
export PORT=${PORT:-9000}
export WAITRESS_THREADS=${WAITRESS_THREADS:-8}
export LOG_LEVEL=${LOG_LEVEL:-info}

# Create logs directory
mkdir -p logs

# Start Waitress
echo "Starting Waitress with $WAITRESS_THREADS threads on port $PORT"
exec waitress-serve \
    --host=0.0.0.0 \
    --port=$PORT \
    --threads=$WAITRESS_THREADS \
    wsgi:application
