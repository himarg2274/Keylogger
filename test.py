# -------------------- IMPORT LIBRARIES -------------------- #

import time
from pynput.keyboard import Controller

keyboard = Controller()

# -------------------- TEST DATA -------------------- #

test_sentences = [
    "This is a keylogger testing script",
    "End of keylogger test"
]

print("Starting automated typing test...")
time.sleep(5)  # time to switch to another window if needed

# -------------------- TYPE SENTENCES -------------------- #

for sentence in test_sentences:

    for char in sentence:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.05)

    keyboard.press(" ")
    keyboard.release(" ")

print("Typing test completed.")