#!/bin/bash

echo "Starting backend image..."
docker run -d -p 8000:8000 amazon/dynamodb-local

echo "Starting python env..."
source /c/projects/fridge-runner/fridge-runner/backend/service-layer-python/Scripts/activate

echo "Starting SAM..."
cd /c/projects/fridge-runner/fridge-runner/backend/lambda-service/fridge-runner
sam.cmd build
sam.cmd local start-api --docker-network host -p 3001 &

#echo "Building docker image for frontend..."
#cd /c/projects/fridge-runner/fridge-runner/frontend
# docker-compose build --no-cache
# docker-compose up -d

#Switched to just running frontend locally 
# cd /c/projects/fridge-runner/fridge-runner/frontend/fridge-runner
# npm start


echo "Dev Env Running..."
