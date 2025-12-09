#!/bin/bash
echo "Starting backend server..."
cd /home/ubuntu/backend
gunicorn app:app --bind 0.0.0.0:5000 --workers 3
