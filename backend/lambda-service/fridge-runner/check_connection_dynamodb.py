import boto3 

dynamodb = boto3.resource('dynamodb', endpoint_url = 'http://localhost/:8080')
table_name = 'TestTable'

try:
    table = dynamodb.Table(table_name)
    print(f"Table {table_name} exists and is accessible.")
    response = table.scan()
    print(f"Items in {table_name}: {response.get('Items', [])}")
except Exception as e:
    print(f"Error accessing table: {e}")