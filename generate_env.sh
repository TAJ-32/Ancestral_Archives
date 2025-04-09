#!/bin/bash

POSTGRES_DB="ancestral_archives"
POSTGRES_USER="postgres"

# Generate random Postgres password (32 characters)
POSTGRES_PASSWORD=$(openssl rand -base64 32 | tr -dc 'a-zA-Z0-9' | head -c 32)

# Generate Django secret key (50 characters)
DJANGO_SECRET_KEY=$(openssl rand -base64 64 | tr -dc 'a-zA-Z0-9!@#$%^&*(-_=+)' | head -c 50)

# Output to .env.example
cat > ./backend/.env <<EOF
POSTGRES_DB=$POSTGRES_DB
POSTGRES_USER=$POSTGRES_USER
POSTGRES_PASSWORD=$POSTGRES_PASSWORD
DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
EOF

echo ".env.example file generated successfully."