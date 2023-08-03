#!/bin/bash

# This script pulls the Juice Shop Docker image and stars the container on port 3000
# If you wnat to run the container in the foreground, remove the -d flag in the docker run command

echo "Pulling image..."
docker pull bkimminich/juice-shop

echo "Running container in detached mode..."
docker run -d --rm -p 3000:3000 bkimminich/juice-shop

echo "Container started"
echo "Visit Juice Shop on http://localhost:3000"
