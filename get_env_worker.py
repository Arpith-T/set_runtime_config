import json

from get_worker_guid import get_worker_guid
import requests
from cf_oauth_token import aciat001_oauth_token


def get_env_worker():
    url = f"https://api.cf.sap.hana.ondemand.com/v3/apps/{get_worker_guid()}/environment_variables"

    payload = {}
    headers = {
        'Authorization': f'{aciat001_oauth_token()}',
        'Cookie': 'JTENANTSESSIONID_kr19bxkapa=FPtRDK1dM3D1lD56pq9oAq9mvHn19ohxqXjClhqrbLI%3D'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(json.dumps(response.json(), indent=4))

    return json.loads(response.text)

    # print(type(json.loads(response.text)))



# get_env_worker()