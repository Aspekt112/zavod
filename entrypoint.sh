#!/bin/sh
python manage.py makemigrations zavod
python manage.py migrate
exec "$@"
