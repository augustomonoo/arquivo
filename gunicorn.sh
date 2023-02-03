#!/bin/sh

./manage.py migrate
# ./manage.py initadmin && \
# ./manage.py send_queued_messages

if [ $? -ne 0 ]
then
    exit 1
fi

exec gunicorn config.wsgi:application \
    --pythonpath $(pwd) \
    --name config \
    --bind unix:/tmp/gunicorn.sock \
    --bind :8000 \
    --workers "${GUNICORN_WORKERS?Número de workers não definido}" \
    --log-level=info \
    --access-logfile='-' \
    "$@"