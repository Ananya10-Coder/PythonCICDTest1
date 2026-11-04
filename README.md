# AWS Python CI/CD Demo

A tiny Flask application for testing a GitHub Actions pipeline that deploys to AWS Elastic Beanstalk.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python application.py
```

Open http://127.0.0.1:5000 or http://127.0.0.1:5000/health.

## Run tests

```bash
pytest -q
```

## Elastic Beanstalk notes

- Platform: Python on Amazon Linux 2023
- WSGI entry point: `application:application`
- Application entry file: `application.py`

The Flask object is deliberately named `application` to match the Elastic Beanstalk Python platform's default WSGI entry point.

## CI/CD test

Change the message in `application.py`, run the tests, commit, and push to the branch configured in your GitHub Actions workflow.
