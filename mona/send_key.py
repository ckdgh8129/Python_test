import pyautogui
import sys
import time

# VSeeFace가 인식할 수 있게 0.1초 동안 꾹 눌렀다 뗍니다.
key = sys.argv[1]
pyautogui.keyDown(key)
time.sleep(0.1) 
pyautogui.keyUp(key)