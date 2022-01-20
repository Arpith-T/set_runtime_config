import requests
import json

def read_config():
    with open('config.json') as data_file:
        config_file = json.load(data_file)
    return config_file


config_file = read_config()
tenant = config_file["payload"]["scopeId"]
base_url = config_file["base_url"]

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