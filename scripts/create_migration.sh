#!/bin/bash
# Скрипт для создания новой миграции

if [ -z "$1" ]; then
    echo "Usage: ./create_migration.sh \"migration message\""
    exit 1
fi

echo "Creating migration: $1"
docker compose exec alembic_migration alembic revision --autogenerate -m "$1"
if [ $? -eq 0 ]; then
    echo "Migration created successfully!"
else
    echo "Failed to create migration!"
    exit 1
fi