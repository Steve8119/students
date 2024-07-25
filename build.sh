#!/bin/bash

# Exit on error
set -e

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the Django application
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
