from flask import Flask, request, jsonify
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)

dynamodb = boto3.resource(
    'dynamodb', 
    endpoint_url='http://localhost:8000', 
    region_name='us-west-2',
    #NB - Only 1-9 a-z in these - no special chars as of 2023-06-28
    aws_access_key_id='dummyaccesskey', 
    aws_secret_access_key='dummysecretkey'
    )

table_name = 'test-table'

try:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'testString',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'testString',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
    print(f"Table Created: '{table_name}'")
    
except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceInUseException':
        table = dynamodb.Table(table_name)
        print(f"Table '{table_name}' already exists.")
    else:
        raise

@app.route('/test', methods=['GET'])
def test_route():
    return jsonify({"message": "Flask service layer is working."})

if __name__ == '__main__':
    app.run(debug=True)