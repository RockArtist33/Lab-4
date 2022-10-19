import pyautogui
import time

time.sleep(3)

for index in range(0,1000):
    mouse_x,mouse_y = pyautogui.position()
    
    pyautogui.click(mouse_x,mouse_y)