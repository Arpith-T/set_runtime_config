import requests
import json
from get_trm_token import aciat001_trm_token


def read_config():
    with open('config.json') as data_file:
        config_file = json.load(data_file)
    return config_file
config_file = read_config()
tenant = config_file["payload"]["scopeId"]
base_url = config_file["base_url"]


def get_runtime_config():
    url = f"{base_url}/api/trm/v1/configurations?scope=TENANT&entity=workerset.vmargs&scopeId={tenant}"

    payload = json.dumps(config_file["payload"])
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {aciat001_trm_token()}',
        'Cookie': 'JTENANTSESSIONID_kr19bxkapa=FPtRDK1dM3D1lD56pq9oAq9mvHn19ohxqXjClhqrbLI%3D'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(json.dumps(response.json(), indent=4))

    return response

get_runtime_config()