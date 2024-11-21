#!/bin/bash

echo "Stopping existing instances..."
PIDSs=$(netstat -aon | grep ":$PORT" | awk '{print $5}')
if [ ! -z "$PIDs" ]; then
    echo "Killing processes: $PIDs"
    echo "$PIDs" | xargs -n 1 taskkill //PID > /dev/null 2>&1
else 
    echo "No SAM CLI instances found"
fi 

cd /c/projects/fridge-runner/fridge-runner/backend/lambda-service/fridge-runner

TEMPLATE_FILE = "template.yaml"
PORT=3001

echo "Building SAM template..."
sam.cmd build

echo "Restarting SAM CLI..."
start "" "C:\Program Files\Git\bin\bash.exe" --login -c "cd /c/projects/fridge-runner/fridge-runner/backend/lambda-service/fridge-runner && sam.cmd local start-api -p $PORT; exec bash"

