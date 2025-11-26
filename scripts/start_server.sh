#!/bin/bash
pkill -f "python3 app.py" || true
cd /home/ubuntu/backend
nohup python3 app.py > app.log 2>&1 &
