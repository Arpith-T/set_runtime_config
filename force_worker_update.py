from get_trm_token import aciat001_trm_token
import json


def read_config():
    with open('config.json') as data_file:
        config_file = json.load(data_file)
    return config_file


config_file = read_config()
tenant = config_file["payload"]["scopeId"]
base_url = config_file["base_url"]


def force_worker_update():
    import requests

    url = f"https://it-aciat001-trm.cfapps.sap.hana.ondemand.com/api/trm/v1/tenant-softwares/tenants?tenantNames={tenant}"

    payload = {}
    headers = {
        'Authorization': f'Bearer {aciat001_trm_token()}',
        'Cookie': 'JTENANTSESSIONID_kr19bxkapa=FPtRDK1dM3D1lD56pq9oAq9mvHn19ohxqXjClhqrbLI%3D'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(json.dumps(response.json(), indent=4))


def main():
    force_worker_update()


if __name__ == "__main__":
    main()
