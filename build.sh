#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Print each command before executing it
set -x

# Ensure the Python environment is active (if using virtualenv or conda)
# source path/to/your/virtualenv/bin/activate

# Install dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
elif [ -f "pyproject.toml" ]; then
    poetry install
else
    echo "No requirements file found"
    exit 1
fi

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Run any custom build tasks (e.g., linting, testing)
# python manage.py test
