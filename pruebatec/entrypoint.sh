#!/bin/ash

echo "Apply database migrations"
ṕython manage.py migrate

exec "$@"