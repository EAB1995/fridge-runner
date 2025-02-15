import json
import boto3
from botocore.exceptions import ClientError

#Original
#dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

#Suggested change after troubleshooting internal docker container connectivity
dynamodb = boto3.resource('dynamodb', endpoint_url='http://host.docker.internal:8000')


TABLE_NAME = 'TestTable'

#Call lambda with curl: 
# curl -X OPTIONS http://127.0.0.1:3001/save-input -i

#With payload: 
# curl -X POST http://127.0.0.1:3001/save-input \
#   -H "Content-Type: application/json" \
#   -d '{"ItemId": "4", "TestValue": "SampleData4"}' -i


def lambda_handler(event, context):
    print("\nPOST lambda_handler app.py fridge-runner > save_input\n")
    print("\nSave input start...\n")
    print("Received event:", json.dumps(event, indent=2))
    headers = {
        "Content-Type": "application/json",
        "X-Custom-Header": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "X-Requested-With,content-type, Content-Type"
    }
    #^Try adding X-Requested-With on next go
    # from this post https://stackoverflow.com/questions/53312412/enable-cors-when-running-aws-sam-cli-locally
    #^ Added Api: to Globals in yaml and X-Requested-With,content-type, X-Custom-Header above 

    if event['httpMethod'] == 'OPTIONS':
        print("OPTIONS test")
        return {
            "statusCode": 200,
            "headers": headers,
            "body":json.dumps('Preflight OK')
        }
    
    if event['httpMethod'] == 'POST':
        print("\nPOST Request received...\n")
        try:
            body = json.loads(event['body'])
            item_id = body.get("ItemId")
            test_value = body.get("TestValue")

            response_msg_received = f"Received ItemId: {item_id}, TestValue: {test_value}"
            print("\nResponse Message: ", response_msg_received, "\n")
            table = dynamodb.Table(TABLE_NAME)
            table.put_item(
                Item = {
                    'ItemId': item_id,
                    'TestValue': test_value
                }
            )

            response_msg_svd = f"Successfully saved ItemId: {item_id}"
            print("Response Message: ", response_msg_svd)
            return {
                "statusCode": 200,
                "headers": headers,
                "body": json.dumps({"message": response_msg_svd})
            }
        
        except (json.JSONDecodeError, KeyError) as e:
            return {
                "statusCode": 400,
                "headers": headers,
                "body": json.dumps({"error": "Invalid input", "details": str(e)})
            }
        
        except ClientError as e:
            print("DynamoDb Error: ", e)
            return {
                "statusCode": 500,
                "headers": headers,
                "body": json.dumps({"error": "Failed to save"})
            }
        
    print("\nUnsupported method received\n")

    return {
        "statusCode": 405,
        "headers": headers,
        "body": json.dumps({"error": "Method not allowed"})
    }

