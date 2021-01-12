"""
simple spamming bot

before using it --> install pynput

pip install pynput
"""
from pynput.keyboard import Key, Controller
import time

message = "spamming"
keyboard = Controller()

time.sleep(10)

for num in range(50):
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
