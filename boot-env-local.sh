#!/bin/bash

printf "\nStarting backend image...\n"
docker run -d -p 8000:8000 amazon/dynamodb-local

printf "\nStarting python env...\n"
source /c/projects/fridge-runner/fridge-runner/backend/lambda-service/fridge-runner/venv/Scripts/activate

printf "\nStarting SAM locally...\n"
cd /c/projects/fridge-runner/fridge-runner/backend/lambda-service/fridge-runner
sam.cmd build
#sam.cmd local start-api -p 3001 &
#Start SAM CLI gateway bound to ALL interfaces
sam.cmd local start-api -p 3001 --host 0.0.0.0 --debug &


printf "\nStarting frontend...\n"
cd /c/projects/fridge-runner/fridge-runner/frontend/fridge-runner
npm start

printf "\nBuilding test tables...\n"
cd /c/projects/fridge-runner/fridge-runner/fridge-runner/backend
./test-table-create.sh

#Not being called currently
printf "\nGetting test tables...\n"
cd /c/projects/fridge-runner/fridge-runner/fridge-runner/backend
./test-table-get.sh

printf "\nDev Env Running...\n"