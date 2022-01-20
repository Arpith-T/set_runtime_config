import json
import requests


def read_config():
    with open('config.json') as data_file:
        config_file = json.load(data_file)
    return config_file
config_file = read_config()

def aciat001_trm_token():
    url = "https://aciat001.authentication.sap.hana.ondemand.com/oauth/token?grant_type=client_credentials"

    payload = {}
    files = {}
    headers = {
        'Authorization': 'Basic c2ItaXQhYjc2NDg6ZmIyMGZmYzktMDFjNy00ZTY2LTk2ODAtMjk3YzU3ZWY0ZTYzJEduMEtEeFYtd2Q4NTNTWTNJVXBjeElOSWU3UzhpRjZhZ3Jsdll0aXdhTE09'
    }

    response = requests.request("GET", url, headers=headers, data=payload, files=files)

    # print(response.text)
    # print("\n")
    # print(type(response.text))
    res_in_dict = json.loads(response.text)
    return res_in_dict["access_token"]

def set_runtime_config():
    import requests
    import json

    url = "https://it-aciat001-trm.cfapps.sap.hana.ondemand.com/api/trm/v1/configurations"

    payload = json.dumps({
        "configurationParameters": [
            {
                "entity": "workerset.vmargs",
                "key": "com.sap.it.messaging.jms.connection.pool",
                "value": "true",
                "values": [],
                "valueType": "SINGLE"
            }
        ],
        "scope": "TENANT",
        "scopeId": "iat-aws-h"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {aciat001_trm_token()}',
        'Cookie': 'JTENANTSESSIONID_kr19bxkapa=FPtRDK1dM3D1lD56pq9oAq9mvHn19ohxqXjClhqrbLI%3D'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)




print(config_file["payload"])

