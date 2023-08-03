#!/bin/bash

# This script pulls the DVWA Docker image and stars the container on port 3000
# If you wnat to run the container in the foreground, remove the -d flag in the docker run command

echo "Pulling image..."
docker pull vulnerables/web-dvwa

echo "Running container in detached mode..."
docker run -d --rm -p 80:80 vulnerables/web-dvwa

echo "Container started"
echo "Visit DVWA on http://localhost:80"
