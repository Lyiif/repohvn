#broken smh
import keyboard
import pyperclip
import pyautogui
import time
from datetime import datetime
shortcut = 'alt+t'
#Wednesday January 26th, 2022 10:00 AM EST
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'monday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
def on_triggered():
    pyautogui.typewrite('any text you want to type')
    text = pyperclip.paste().lower()
    print(text)
while True:
    if "th," in pyperclip.paste() and ":" in pyperclip.paste():
        words = pyperclip.paste().split(" ")
        faketime = datetime(2022, months.index(words[1])+1, int(words[2].replace("th,", "")))#words[2].replace("th", "")
        print('norm')
        time.sleep(1000)
    else:
        time.sleep(0.5)

print("Press home to stop.")
