#!/bin/bash
set -e

cd /home/ec2-user/PythonCICDTest1

python3 -m venv venv
venv/bin/pip install -r requirements.txt