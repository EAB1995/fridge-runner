

printf "\nRunning dynamodb list-tables...\n"
aws dynamodb list-tables --endpoint-url http://localhost:8000

printf "\nRunning dynamodb scan...\n"
aws dynamodb scan --table-name TestTable --endpoint-url http://localhost:8000
