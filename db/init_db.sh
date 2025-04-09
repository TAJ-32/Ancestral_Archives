#!/bin/bash
# init.sh - Substitute the environment variables and run SQL

# Substitute environment variables into the SQL file
envsubst < /docker-entrypoint-initdb.d/init.sql > /docker-entrypoint-initdb.d/init_with_values.sql

# Run the SQL file that has the substituted values
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f /docker-entrypoint-initdb.d/init_with_values.sql
