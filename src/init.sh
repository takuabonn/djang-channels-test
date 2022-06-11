#!/bin/sh
chmod 744 init.sh
python manage.py migrate
# uwsgi --socket :8001 --module config.wsgi --py-autoreload 1
daphne -b 0.0.0.0 -p 8002 config.asgi:application

