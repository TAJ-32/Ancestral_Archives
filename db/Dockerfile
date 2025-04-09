# db/Dockerfile
FROM postgres:latest

# Copy script into the image
COPY init_db.sh /docker-entrypoint-initdb.d/init_db.sh
RUN chmod +x /docker-entrypoint-initdb.d/init_db.sh

RUN apt-get update && apt-get install -y gettext && rm -rf /var/lib/apt/lists/*
