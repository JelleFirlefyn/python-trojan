from send_file import send_file
from removefile import removefile
import os
import pyautogui

FOLDER_NAME = "content"
FILE_NAME = "screenshot.png"
FILE_PATH = os.path.join(FOLDER_NAME, FILE_NAME)


class screenshot():
    def __init__(self):
        self.screenshot = pyautogui.screenshot()
    
    def save(self):
        if not os.path.exists(FOLDER_NAME):
            os.makedirs(FOLDER_NAME)
        
        self.screenshot.save(FILE_PATH)

    def send(self):
        send_file(FILE_PATH)

    def remove(self):
        removefile(FILE_PATH)