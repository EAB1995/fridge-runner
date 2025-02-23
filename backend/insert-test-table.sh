#Insert test item in Test Table
aws dynamodb put-item --table-name TestTable --item '{"ItemId": {"S": "3"}, "Name": {"S": "Butter"}, "Quantity": {"N": "1"}}' --endpoint-url http://localhost:8000
#Log contents of Test Table
aws dynamodb scan --table-name TestTable --endpoint-url http://localhost:8000