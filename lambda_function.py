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
    
    try:
        response = http.request('POST',
            "https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data",
            headers=headers,
            json=payload
        )
        
        print(f"Response Status: {response.status}")
        print(f"Response Data: {response.data}")
        
        return {
            "statusCode": response.status,
            "body": response.data.decode('utf-8')
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps("An error occurred: " + str(e))
        }
