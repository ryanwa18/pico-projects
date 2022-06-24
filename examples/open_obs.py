# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Button example for Pico. Does a spotlight search for OBS and opens the app.

REQUIRED HARDWARE:
* Button switch on pin GP13.
"""
import time
import board
import digitalio

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

while True:
    if button.value:
        keyboard.press(Keycode.COMMAND, Keycode.SPACE)
        keyboard.release_all()
        keyboard_layout.write("obs")
        keyboard.press(Keycode.ENTER)
        keyboard.release_all()
        print("Opening OBS....")
    time.sleep(0.5)