import pyautogui
import time

time.sleep(6)

screenshot = pyautogui.screenshot()
screenshot.save("screenshot1.png")
