"""
Waitress configuration for production deployment
Cross-platform WSGI server configuration
"""

import os

# Server configuration
host = "0.0.0.0"
port = int(os.getenv('PORT', 9000))

# Performance settings
threads = int(os.getenv('WAITRESS_THREADS', 8))
connection_limit = int(os.getenv('WAITRESS_CONNECTION_LIMIT', 1000))
cleanup_interval = int(os.getenv('WAITRESS_CLEANUP_INTERVAL', 30))

# Timeout settings
recv_bytes = int(os.getenv('WAITRESS_RECV_BYTES', 65536))
send_bytes = int(os.getenv('WAITRESS_SEND_BYTES', 18000))

# Channel timeout (in seconds)
channel_timeout = int(os.getenv('WAITRESS_CHANNEL_TIMEOUT', 120))

# Application module
application_module = "wsgi:application"

def get_waitress_args():
    """Get Waitress command line arguments"""
    return [
        f"--host={host}",
        f"--port={port}",
        f"--threads={threads}",
        f"--connection-limit={connection_limit}",
        f"--cleanup-interval={cleanup_interval}",
        f"--recv-bytes={recv_bytes}",
        f"--send-bytes={send_bytes}",
        f"--channel-timeout={channel_timeout}",
        application_module
    ]

if __name__ == "__main__":
    print("Waitress Configuration:")
    print(f"  Host: {host}")
    print(f"  Port: {port}")
    print(f"  Threads: {threads}")
    print(f"  Connection Limit: {connection_limit}")
    print(f"  Application: {application_module}")
