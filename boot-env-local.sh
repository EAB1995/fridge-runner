#!/bin/bash

#TODO###############
# We are trying to set up the python virtual env in /lambda-service/fridgerunnner, 
# as before the env was loaded in to /service-layer-python, which was the old Flask directory (now deleted).
# This is to ifx an issue with check_connection_dynamodb.py, which is unable to import boto3, which I suspect is 
# because of the duelling virtual envs. 

# We are trying to audit the dynamo db connection outside of the AWS CLI context to see if it can be reached
# and troubleshoot the networking, as save_input.py is the first lambda to try and actually reach the db, 
# whereas hello world is only reaching the lambda layer, and not trying to actually post to dynamo. 

printf "\nStarting backend image...\n"
docker run -d -p 8000:8000 amazon/dynamodb-local

printf "\nStarting python env...\n"
#Not sure if this line is redundant now that the python env seems activated by default (Ctrl + Shft + P). 
#Also not sure if this is activating properly as part of this startup script
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

printf "\nGetting test tables...\n"
cd /c/projects/fridge-runner/fridge-runner/fridge-runner/backend
./test-table-get.sh

printf "\nDev Env Running...\n"