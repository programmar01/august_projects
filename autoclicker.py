import pyautogui
import keyboard

while True:
    if keyboard.is_pressed("f6"):
            while True: 
                pyautogui.click()
                if keyboard.is_pressed("f7"):
                    break
    else:
        print("F6 not pressed")