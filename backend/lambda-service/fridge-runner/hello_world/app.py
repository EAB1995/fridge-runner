import json

import requests


def lambda_handler(event, context):
    print("GET lambda_handler test print")
    if event['httpMethod'] == 'OPTIONS':
        print("GET lambda_handler test print 2")
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",  
                "Access-Control-Allow-Methods": "GET, OPTIONS",  
                "Access-Control-Allow-Headers": "Content-Type"   
            },
            "body":json.dumps('Preflight OK')
        }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps({
            #This will print on the web console in the reponse tab
            "message": "hello world 1",
            # "location": ip.text.replace("\n", "")
        }),
    }
