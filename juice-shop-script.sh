#!/bin/bash

echo "Pulling image..."
docker pull bkimminich/juice-shop

echo "Running container..."
docker run --rm -p 3000:3000 bkimminich/juice-shop

echo "Container started"
echo "Visit Juice Shop on http://localhost:3000"
