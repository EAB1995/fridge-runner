aws dynamodb create-table \
    --table-name TestTable \
    --attribute-definitions AttributeName=ItemId,AttributeType=S \
    --key-schema AttributeName=ItemId,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --endpoint-url http://localhost:8000

