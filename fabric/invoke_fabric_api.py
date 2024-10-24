
import requests
import json
from requests.adapters import HTTPAdapter, Retry
from azure.identity import ClientSecretCredential
import os
from dotenv import load_dotenv
load_dotenv()

def invoke_fabric_api_request(method, uri, payload=None):
    
    API_ENDPOINT = "api.fabric.microsoft.com/v1"
    scope = 'https://api.fabric.microsoft.com/.default'
    tenant_id = os.getenv('tenant_id')
    client_id = os.getenv('client_id')
    client_secret = os.getenv('client_secret')

    auth = ClientSecretCredential(authority = 'https://login.microsoftonline.com/',
                                            tenant_id = tenant_id,
                                            client_id = client_id,
                                            client_secret = client_secret)
    access_token = auth.get_token(scope)
    access_token = access_token.token

    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    try:
        url = f"https://{API_ENDPOINT}/{uri}"
            
        session = requests.Session()
        retries = Retry(total=3, backoff_factor=5, status_forcelist=[502, 503, 504])
        adapter = HTTPAdapter(max_retries=retries)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        response = session.request(method, url, headers=headers, json=payload, timeout=240)

        response_details = {
            'status_code': response.status_code,
            'response': response.json() if response.content else {},
            'headers': dict(response.headers) 
        }
        print(json.dumps(response_details, indent=2))

    except requests.RequestException as ex:
        print(ex)