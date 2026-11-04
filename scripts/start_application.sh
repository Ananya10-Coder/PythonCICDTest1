#!/bin/bash
set -e

cd /home/ec2-user/PythonCICDTest1

# Stop any previously running application, if present
pkill -f '[p]ython application.py' || true

nohup venv/bin/python application.py \
    > /var/log/python-app.log 2>&1 &