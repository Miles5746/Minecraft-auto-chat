print("To whoever is reading this, please run [pip3 install scapy] in terminal and give terminal accessibility of your computer. Thank you for using this script. -By Miles5746")

from pynput import keyboard
import pyautogui
import time

Response = input('What should I say?')
activatechat = ["t", Response]
text = "".join(activatechat)
delay = float(input('Enter the delay between each keystroke.'))
wait = float(input('Enter the delay between each sentince'))

print("Auto chat is activating in ten seconds. To stop, press cntrl+c in terminal.")
time.sleep(10)

if isinstance(delay, (int, float)):
    while True:
       pyautogui.write(text, interval=delay)
       pyautogui.keyDown('enter')
       time.sleep(wait)
else:
    print("Invalid input. The script will now shut down")
