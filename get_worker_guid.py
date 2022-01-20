import json
import requests
from cf_oauth_token import aciat001_oauth_token

from get_trm_token import aciat001_trm_token


def read_config():
    with open('config.json') as data_file:
        config_file = json.load(data_file)
    return config_file


config_file = read_config()
tenant = config_file["payload"]["scopeId"]
base_url = config_file["base_url"]
space_guid = config_file["space_guid"]
cf_url = config_file["cf_url"]

url = f"{cf_url}/v3/apps?page=1&per_page=1000&space_guids={space_guid}"

payload = {}
headers = {
    'Authorization': aciat001_oauth_token()
}

response = requests.request("GET", url, headers=headers, data=payload)

# TODO convert the string received from above to a dictionary

response_dict = json.loads(response.text)
# with open("all_apps.json", "w") as datafile:
#     json.dump(response_dict, datafile)

resources = response_dict["resources"]

len_of_resources = len(response_dict["resources"])

# TODO  list all the apps

string_of_apps = []
for app in range(0, len_of_resources):
    string_of_apps.append(resources[app]["name"])
    # print(string_of_apps)

# TODO out of the apps collected list the apps starting with itw- and sore it in a list - by matching substring -
#  https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method


for item in string_of_apps:
    if f"itw-{tenant}" in item:
        worker = item


def get_worker_guid():
    url = f"{cf_url}/v3/apps?page=1&per_page=1000&space_guids={space_guid}&names={worker}"

    payload = {}
    headers = {
        'Authorization': aciat001_oauth_token()
    }

    response_for_guid = requests.request("GET", url, headers=headers, data=payload)
    response_guid_dict = json.loads(response_for_guid.text)
    worker_guid = response_guid_dict["resources"][0]["guid"]
    return worker_guid


# get_worker_guid()
