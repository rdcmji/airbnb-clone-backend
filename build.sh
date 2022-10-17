#!/usr/bin/env bash
# exit on error
set -o errexit
poetry env use 3.10.7
poetry install

python manage.py collectstatic --no-input
python manage.py migrate