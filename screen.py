import pyautogui
import uuid
import time

def screen():
    name = '{0}.png'.format(uuid.uuid4())
    pyautogui.screenshot(name)
    print(name)
    time.sleep(60)
    screen()

screen()
