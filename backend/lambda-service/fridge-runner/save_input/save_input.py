import json

def lambda_handler(event, context):
    print("Save input start")
    headers = {
        "Content-Type": "application/json",
        "X-Custom-Header": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "X-Requested-With,content-type, Content-Type"
    }
    #^Try adding X-Requested-With on next go
    # from this post https://stackoverflow.com/questions/53312412/enable-cors-when-running-aws-sam-cli-locally

    if event['httpMethod'] == 'OPTIONS':
        print("OPTIONS test")
        return {
            "statusCode": 200,
            "headers": headers,
            "body":json.dumps('Preflight OK')
        }
    
    if event['httpMethod'] == 'POST':
        print("POST test")
        try:
            body = json.loads(event['body'])
            item_id = body.get("ItemId")
            test_value = body.get("TestValue")

            response_message = f"Received ItemId: {item_id}, TestValue: {test_value}"

            return {
                "statusCode": 200,
                "headers": headers,
                "body": json.dumps({"message": response_message})
            }
        
        except (json.JSONDecodeError, KeyError) as e:
            return {
                "statusCode": 400,
                "headers": headers,
                "body": json.dumps({"error": "Invalid input", "details": str(e)})
            }
    
    return {
        "statusCode": 405,
        "headers": headers,
        "body": json.dumps({"error": "Method not allowed"})
    }

