import pyautogui as pa
import time
import webbrowser
webbrowser.open("https://google.com")
time.sleep(5)
pa.write("how to automate in python")
pa.press("enter")
