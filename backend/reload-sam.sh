#!/bin/bash

printf "\nStopping existing instances...\n"
PIDSs=$(netstat -aon | grep ":$PORT" | awk '{print $5}')
if [ ! -z "$PIDs" ]; then
    printf "\nKilling processes: $PIDs\n"
    printf "$PIDs" | xargs -n 1 taskkill //PID > /dev/null 2>&1
else 
    printf "\nNo SAM CLI instances found\n"
fi 

cd /c/projects/fridge-runner/fridge-runner/backend/lambda-service/fridge-runner

TEMPLATE_FILE = "template.yaml"
PORT=3001

printf "\nBuilding SAM template...\n"
sam.cmd build

printf "\nRestarting SAM CLI...\n"
start "" "C:\Program Files\Git\bin\bash.exe" --login -c "cd /c/projects/fridge-runner/fridge-runner/backend/lambda-service/fridge-runner && sam.cmd local start-api -p $PORT; exec bash"

