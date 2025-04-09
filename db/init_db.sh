#!/bin/bash
set -e

# Wait for PostgreSQL to be ready
until pg_isready -U "$POSTGRES_USER"; do
  sleep 1
done

# Check if the database already exists
DB_EXISTS=$(psql -U "$POSTGRES_USER" -tAc "SELECT 1 FROM pg_database WHERE datname = '$POSTGRES_DB'")
if [ "$DB_EXISTS" != "1" ]; then
  echo "Creating database $POSTGRES_DB..."
  createdb -U "$POSTGRES_USER" "$POSTGRES_DB"
else
  echo "Database $POSTGRES_DB already exists, skipping creation."
fi
