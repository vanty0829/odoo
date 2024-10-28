import pandas as pd
import requests
from requests.adapters import HTTPAdapter, Retry
from azure.identity import ClientSecretCredential
import json
import os
from dotenv import load_dotenv
import yaml
load_dotenv()

tenant_id = os.getenv('tenant_id')
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
# scope= 'offline_access https://api.fabric.microsoft.com/OneLake.ReadWrite.All'
scope= 'offline_access https://analysis.windows.net/powerbi/api/.default'


def set_state(key,value):
    file_name = "./conf.yaml"
    with open(file_name) as f:
        doc = yaml.safe_load(f)
    doc[key] = value
    with open(file_name, 'w') as f:
        yaml.safe_dump(doc, f)

def get_state(key):
    config = yaml.safe_load(open("./conf.yaml"))
    return config[key]

def get_code():
    redirect_uri = 'http://localhost/myapp/'
    response_type = 'code'
    response_mode = 'query'
    # scope = ['https://api.fabric.microsoft.com/OneLake.ReadWrite.All']
    state = '12345'

    # Construct the URL
    url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/authorize'

    # Create the query parameters
    params = {
        'client_id': client_id,
        'response_type': response_type,
        'redirect_uri': redirect_uri,
        'response_mode': response_mode,
        'scope': scope,
        'state': state
    }

    # Make the GET request
    response = requests.get(url, params=params)

    # Print the response URL
    return response.url

def get_token(code=''):
    if code:
        url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'

        # Prepare the data for the request
        data = {
            'client_id': client_id,
            'scope': scope,
            'code': code,
            'redirect_uri': 'http://localhost/myapp/',
            'grant_type': 'authorization_code',
            'client_secret': client_secret  # Only required for web apps
        }

        # Make the POST request
        response = requests.post(url, data=data)

        # Check the response
        if response.status_code == 200:
            token_info = response.json()
            set_state('access_token',token_info['access_token'])
            set_state('refresh_token',token_info['refresh_token'])
            return token_info['access_token']
        else:
            return response.text

    else:
        url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'

        # Set the data for the POST request
        data = {
            'client_id': client_id,
            'scope': scope,
            'refresh_token': get_state('refresh_token'),  # Replace with your refresh token
            'grant_type': 'refresh_token',
            'client_secret': client_secret  # Replace with your client secret if required
        }

        # Make the POST request
        response = requests.post(url, data=data)

        set_state('access_token',response.json()['access_token'])
        set_state('refresh_token',response.json()['refresh_token'])
        return response.json()['access_token']

def fabric_api(method, uri, payload=None):
    
    API_ENDPOINT = "api.fabric.microsoft.com/v1"
    access_token = get_token()

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
        return json.dumps(response_details, indent=2)

    except requests.RequestException as ex:
        return ex

def fabric_create_shortcut(from_ws,from_lk,from_path,to_ws,to_lk,to_path,name):
    method = "post"
    shortcut_conflict_policy = "GenerateUniqueName"

    uri = f"workspaces/{to_ws}/items/{to_lk}/shortcuts?shortcutConflictPolicy={shortcut_conflict_policy}"

    payload = {
        "path": to_path,
        "name": name,
        "target": {
            "oneLake": {
            "workspaceId": from_ws,
            "itemId": from_lk,
            "path": from_path
            }
        }
    }
    return fabric_api(method, uri, payload)