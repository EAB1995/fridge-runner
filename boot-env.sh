#!/bin/bash

echo "Building docker image for frontend..."
cd /c/projects/fridge-runner/fridge-runner/frontend
docker build -t fridge-runner-frontend

echo "Starting image..."
docker run -d -p 3000:80 fridge-runner-frontend

echo "Starting backend image..."
docker run -d -p 8000:8000 amazon/dynamodb-local

echo "Starting python env..."
source /c/projects/fridge-runner/fridge-runner/backend/service-layer-python/Scripts/activate

echo "Starting Flask..."
cd /c/projects/fridge-runner/fridge-runner/backend/service-layer-python
flask run

echo "Goodbye."
