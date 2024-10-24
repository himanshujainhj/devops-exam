import json
import urllib3

http = urllib3.PoolManager()

def lambda_handler(event, context):
    subnet_id = event.get('subnet_id')  # Use .get() to handle missing keys
    if not subnet_id:
        return {
            "statusCode": 400,
            "body": json.dumps("Missing required field 'subnet_id'")
        }

    payload = {
        "subnet_id": subnet_id,
        "name": "Himanshu Jain",
        "email": "jainhimanshu207@gmail.com"
    }
    
    headers = {'X-Siemens-Auth': 'test'}
    
    try:
        # Convert the payload to JSON string
        response = http.request(
            'POST',
            "https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data",
            headers=headers,
            body=json.dumps(payload)  # Use body, not json
        )
        
        print(f"Response Status: {response.status}")
        print(f"Response Data: {response.data.decode('utf-8')}")
        
        return {
            "statusCode": response.status,
            "body": response.data.decode('utf-8')
        }
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps(f"An error occurred: {str(e)}")
        }
