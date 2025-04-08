#!/bin/bash

# Make sure generate_env.sh is executable
chmod +x generate_env.sh

# Generate .env
./generate_env.sh

# Build and run Docker containers
docker-compose up --build
