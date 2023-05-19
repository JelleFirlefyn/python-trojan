from send_file import send_file
from removefile import removefile
import pyautogui

class screenshot():
    def __init__(self):
        self.screenshot = pyautogui.screenshot()
    
    def save(self):
        self.screenshot.save('/content/screenshot.png')

    def send(self):
        send_file('/content/screenshot.png')

    def remove(self):
        removefile("/content/screenshot.png")