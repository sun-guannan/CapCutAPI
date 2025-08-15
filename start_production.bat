@echo off
REM Production startup script for CapCut API (Windows)

echo Starting CapCut API in production mode...

REM Set default values
if not defined PORT set PORT=9000
if not defined WAITRESS_THREADS set WAITRESS_THREADS=8
if not defined LOG_LEVEL set LOG_LEVEL=info

REM Create logs directory
if not exist logs mkdir logs

REM Start Waitress (cross-platform WSGI server)
echo Starting Waitress with %WAITRESS_THREADS% threads on port %PORT%
waitress-serve --host=0.0.0.0 --port=%PORT% --threads=%WAITRESS_THREADS% wsgi:application
