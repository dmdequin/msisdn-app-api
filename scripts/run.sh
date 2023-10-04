#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py load_msisdn_data

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi