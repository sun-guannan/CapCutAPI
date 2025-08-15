# Production Deployment Guide

This guide covers deploying the CapCut API in a production environment using Gunicorn and optional Nginx reverse proxy.

## 🚀 Quick Start

### Option 1: Direct Gunicorn Deployment

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables:**
   ```bash
   # Create .env file or export these variables
   export PORT=9000
   export GUNICORN_WORKERS=4
   export LOG_LEVEL=info
   export REDIS_HOST=localhost
   export REDIS_PORT=6379
   export REDIS_DRAFT_DB=1
   ```

3. **Start production server:**
   ```bash
   # Linux/Mac
   ./start_production.sh
   
   # Windows
   start_production.bat
   
   # Manual
   gunicorn --config gunicorn.conf.py wsgi:application
   ```

### Option 2: Docker Deployment

1. **Build and run with Docker Compose:**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

2. **Check health:**
   ```bash
   curl http://localhost:9000/health
   ```

## 📋 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | 9000 | Server port |
| `GUNICORN_WORKERS` | 4 | Number of worker processes |
| `LOG_LEVEL` | info | Log level (debug/info/warning/error) |
| `REDIS_HOST` | localhost | Redis server host |
| `REDIS_PORT` | 6379 | Redis server port |
| `REDIS_DRAFT_DB` | 1 | Redis database for drafts |
| `DRAFT_TTL_SECONDS` | 86400 | Draft expiration time (24 hours) |
| `MEMORY_CACHE_SIZE` | 100 | In-memory cache size |

### Gunicorn Configuration

The `gunicorn.conf.py` file contains optimized settings for production:

- **Workers**: Auto-calculated based on CPU cores
- **Worker Class**: Gevent for async I/O
- **Timeouts**: 5 minutes for video processing
- **Memory Management**: Auto-restart workers after 1000 requests
- **Logging**: Structured logging to stdout/stderr

## 🔧 Advanced Deployment

### With Nginx Reverse Proxy

1. **Install Nginx:**
   ```bash
   # Ubuntu/Debian
   sudo apt update && sudo apt install nginx
   
   # CentOS/RHEL
   sudo yum install nginx
   ```

2. **Configure Nginx:**
   ```bash
   # Copy the example configuration
   sudo cp nginx.conf.example /etc/nginx/sites-available/capcut-api
   
   # Update domain name and SSL certificates in the file
   sudo nano /etc/nginx/sites-available/capcut-api
   
   # Enable the site
   sudo ln -s /etc/nginx/sites-available/capcut-api /etc/nginx/sites-enabled/
   
   # Test configuration
   sudo nginx -t
   
   # Restart Nginx
   sudo systemctl restart nginx
   ```

3. **SSL Configuration (Recommended):**
   - Update certificate paths in `nginx.conf.example`
   - Use Let's Encrypt for free SSL certificates:
     ```bash
     sudo apt install certbot python3-certbot-nginx
     sudo certbot --nginx -d your-domain.com
     ```

### Systemd Service (Linux)

Create a systemd service for automatic startup:

```bash
sudo nano /etc/systemd/system/capcut-api.service
```

```ini
[Unit]
Description=CapCut API Gunicorn Application
After=network.target

[Service]
User=your-user
Group=your-group
WorkingDirectory=/path/to/your/project
Environment="PATH=/path/to/your/venv/bin"
EnvironmentFile=/path/to/your/.env
ExecStart=/path/to/your/venv/bin/gunicorn --config gunicorn.conf.py wsgi:application
ExecReload=/bin/kill -s HUP $MAINPID
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable capcut-api
sudo systemctl start capcut-api
sudo systemctl status capcut-api
```

## 📊 Monitoring

### Health Checks

The API includes a health check endpoint at `/health`:

```bash
curl http://localhost:9000/health
```

Response:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00",
  "version": "1.0.0",
  "services": {
    "redis": "healthy",
    "api": "healthy"
  }
}
```

### Logging

Logs are written to:
- **Application logs**: `logs/capcut_api.log` (rotating, 10MB max)
- **Gunicorn logs**: stdout/stderr (captured by Docker/systemd)
- **Nginx logs**: `/var/log/nginx/capcut_api_*.log`

### Metrics

Monitor these key metrics:
- Response times (especially for video processing)
- Error rates
- Worker process health
- Redis connection status
- Memory usage
- CPU utilization

## 🔒 Security

### Production Security Checklist

- [ ] Use HTTPS with valid SSL certificates
- [ ] Configure proper firewall rules
- [ ] Set up rate limiting (done in Nginx config)
- [ ] Use strong Redis passwords if exposed
- [ ] Keep dependencies updated
- [ ] Monitor for security vulnerabilities
- [ ] Implement proper logging and monitoring
- [ ] Use non-root user for application
- [ ] Secure file permissions

### Rate Limiting

The Nginx configuration includes rate limiting:
- 10 requests per second per IP
- Burst of 20 requests allowed
- Health check endpoint excluded from rate limiting

## 🚨 Troubleshooting

### Common Issues

1. **Workers timing out:**
   - Increase `timeout` in `gunicorn.conf.py`
   - Monitor video processing operations

2. **High memory usage:**
   - Reduce `MEMORY_CACHE_SIZE`
   - Increase `max_requests` to restart workers more frequently

3. **Redis connection errors:**
   - Check Redis server status
   - Verify connection parameters
   - Check firewall/network connectivity

4. **Slow response times:**
   - Increase number of workers
   - Check Redis performance
   - Monitor system resources

### Log Analysis

```bash
# Check application logs
tail -f logs/capcut_api.log

# Check Gunicorn worker status
ps aux | grep gunicorn

# Check system resources
htop
free -h
df -h

# Check Redis status
redis-cli info

# Check network connections
netstat -tulpn | grep :9000
```

## 📈 Performance Tuning

### Recommended Production Settings

For a server with 4 CPU cores and 8GB RAM:

```bash
# Environment variables
export GUNICORN_WORKERS=8
export MEMORY_CACHE_SIZE=200
export REDIS_DRAFT_DB=1

# Redis optimization
redis-cli config set maxmemory 2gb
redis-cli config set maxmemory-policy allkeys-lru
```

### Scaling

1. **Horizontal scaling:** Deploy multiple instances behind a load balancer
2. **Vertical scaling:** Increase server resources and worker count
3. **Database scaling:** Use Redis Cluster for high availability
4. **CDN:** Use CDN for static assets and video delivery

## 🔄 Updates and Maintenance

### Zero-downtime Deployment

1. **Using Gunicorn reload:**
   ```bash
   # Send HUP signal to reload workers
   kill -HUP $(cat /tmp/gunicorn.pid)
   ```

2. **Using Docker:**
   ```bash
   # Build new image
   docker build -t capcut-api:new .
   
   # Update docker-compose.yml with new tag
   # Rolling update
   docker-compose -f docker-compose.prod.yml up -d
   ```

### Backup and Recovery

1. **Redis data backup:**
   ```bash
   # Create backup
   redis-cli save
   cp /var/lib/redis/dump.rdb backup_$(date +%Y%m%d_%H%M%S).rdb
   ```

2. **Application logs backup:**
   ```bash
   # Archive old logs
   tar -czf logs_backup_$(date +%Y%m%d).tar.gz logs/
   ```

This completes your production deployment setup! 🎉
