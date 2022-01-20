from get_env_worker import get_env_worker
import json


def read_config():
    with open('config.json') as data_file:
        config_file = json.load(data_file)
    return config_file


config_file = read_config()

tenant = config_file["payload"]["scopeId"]
base_url = config_file["base_url"]
prop = config_file["payload"]["configurationParameters"][0]["key"]
env_var = str(get_env_worker())

if prop in env_var:
    print(f"\nThe property '{prop}' is registered on worker '{tenant}'")
else:
    print("check the code properly")
