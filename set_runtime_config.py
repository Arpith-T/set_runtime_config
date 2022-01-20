import json
import time
import requests
from force_worker_update import force_worker_update
from get_trm_token import aciat001_trm_token


def read_config():
    with open('config.json') as data_file:
        config_file = json.load(data_file)
    return config_file


config_file = read_config()
base_url = config_file["base_url"]
# print(base_url)
tenant = config_file["payload"]["scopeId"]


# print(tenant)

def set_runtime_config():
    url = f"{base_url}/api/trm/v1/configurations"

    payload = json.dumps(config_file["payload"])
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {aciat001_trm_token()}',
        'Cookie': 'JTENANTSESSIONID_kr19bxkapa=FPtRDK1dM3D1lD56pq9oAq9mvHn19ohxqXjClhqrbLI%3D'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    if response.status_code == 200:
        print(f"configuration is updated on {tenant}. worker update on {tenant} will be triggered now and will be changes will be implemented post the update")
    else:
        print("configuration not set retry again or check what might have gone wrong")


# set_runtime_config()
# time.sleep(30)
# force_worker_update()

def main():
    set_runtime_config()
    time.sleep(10)
    force_worker_update()


if __name__ == "__main__":
    main()
