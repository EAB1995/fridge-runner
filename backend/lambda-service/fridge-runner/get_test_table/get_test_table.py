import json
import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url='http://host.docker.internal:8000')

TABLE_NAME = 'TestTable'

def lambda_handler(event, context):
    print("\nGET lambda_handler get_test_table.py fridge-runner > get_test_table\n")

    headers = {
        "Content-Type": "application/json",
        "X-Custom-Header": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Access-Control-Allow-Headers": "X-Requested-With,content-type, Content-Type"
    }

    if event['httpMethod'] == 'OPTIONS':
        print("OPTIONS test")
        return {
            "statusCode": 200,
            "headers": headers,
            "body":json.dumps('Preflight OK')
        }
    
    if event['httpMethod'] == 'GET':
        print("\nGET Request received...\n")
        try:
            table = dynamodb.Table(TABLE_NAME)
            itemCount = table.item_count
            tableScan = table.scan()
            print("\nTOTAL ITEMS: ", itemCount)
            print("\nLOGGING:", TABLE_NAME, ":\n", tableScan)
        
        except (json.JSONDecodeError, KeyError) as e:
            return {
                "statusCode": 400,
                "headers": headers,
                "body": json.dumps({"error": "Invalid Request", "details": str(e)})
            }

    return {
        "statusCode": 200,
        "body": json.dumps({"message": tableScan}),
    }
