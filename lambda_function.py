import json
import urllib3

http = urllib3.PoolManager()

def lambda_handler(event, context):
    subnet_id = event['subnet_id']
    payload = {
        "subnet_id": subnet_id,
        "name": "Himanshu Jain",
        "email": "jainhimanshu207@gmail.com"
    }
    headers = {'X-Siemens-Auth': 'test'}
    response = http.request('POST',
        "https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data",
        headers=headers,
        json=payload
    )
    return {
        "statusCode": response.status_code,
        "body": response.text
    }
