# # Import the libraries
import board
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

import time
#
# # define output LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
#
# flash the LED when booting
for x in range(0, 3):
    led.value = False
    time.sleep(0.2)
    led.value = True
    time.sleep(0.2)

# configure device as keyboard
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# define buttons
d0 = DigitalInOut(board.D0)
d0.direction = Direction.INPUT
d0.pull = Pull.UP

d1 = DigitalInOut(board.D1)
d1.direction = Direction.INPUT
d1.pull = Pull.UP

d2 = DigitalInOut(board.D2)
d2.direction = Direction.INPUT
d2.pull = Pull.UP

d3 = DigitalInOut(board.D3)
d3.direction = Direction.INPUT
d3.pull = Pull.UP

d4 = DigitalInOut(board.D4)
d4.direction = Direction.INPUT
d4.pull = Pull.UP

d5 = DigitalInOut(board.D5)
d5.direction = Direction.INPUT
d5.pull = Pull.UP

d6 = DigitalInOut(board.D6)
d6.direction = Direction.INPUT
d6.pull = Pull.UP

d7 = DigitalInOut(board.D7)
d7.direction = Direction.INPUT
d7.pull = Pull.UP

d8 = DigitalInOut(board.D8)
d8.direction = Direction.INPUT
d8.pull = Pull.UP

d9 = DigitalInOut(board.D9)
d9.direction = Direction.INPUT
d9.pull = Pull.UP

d10 = DigitalInOut(board.D10)
d10.direction = Direction.INPUT
d10.pull = Pull.UP

# little function to open apps via spotlight
# def open_app(app):
#     kbd.send(Keycode.COMMAND, Keycode.SPACE)
#     time.sleep(0.2)
#     layout.write(app)
#     time.sleep(0.2)
#     kbd.send(Keycode.ENTER)

# loop forever
while True:

    # left col
    if not d0.value:
        led.value = False # led on
        for x in range(0, 2):
            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.WINDOWS)
            kbd.press(Keycode.LEFT_ARROW)
            kbd.release_all()
            time.sleep(0.05)
        time.sleep(0.2)
        led.value = True # led off

    if not d2.value:
        led.value = False # led on
        for x in range(0, 2):
            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.WINDOWS)
            kbd.press(Keycode.LEFT_ARROW)
            kbd.release_all()
            time.sleep(0.05)

        for x in range(0, 1):
            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.WINDOWS)
            kbd.press(Keycode.RIGHT_ARROW)
            kbd.release_all()
        time.sleep(0.2)
        led.value = True # led off

    if not d4.value:
        led.value = False # led on
        for x in range(0, 2):
            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.WINDOWS)
            kbd.press(Keycode.LEFT_ARROW)
            kbd.release_all()
            time.sleep(0.05)
            
        for x in range(0, 2):
            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.WINDOWS)
            kbd.press(Keycode.RIGHT_ARROW)
            kbd.release_all()
        time.sleep(0.2)
        led.value = True # led off

    if not d6.value:
        led.value = False # led on
        kbd.press(Keycode.CONTROL)
        kbd.press(Keycode.WINDOWS)
        kbd.press(Keycode.LEFT_ARROW)
        kbd.release_all()
        time.sleep(0.2)
        led.value = True # led off

    # right col
    if not d7.value:
        led.value = False # led on
        layout.write('d7')
        time.sleep(0.2)
        led.value = True # led off

    if not d8.value:
        led.value = False # led on
        kbd.send(Keycode.WINDOWS, Keycode.L)
        time.sleep(0.2)
        led.value = True # led off

    if not d9.value:
        led.value = False # led on
        # layout.write('d9')
        kbd.send(Keycode.WINDOWS, Keycode.D)
        time.sleep(0.2)
        led.value = True # led off

    if not d10.value:
        led.value = False # led on
        kbd.press(Keycode.CONTROL)
        kbd.press(Keycode.WINDOWS)
        kbd.press(Keycode.RIGHT_ARROW)
        kbd.release_all()
        time.sleep(0.2)
        led.value = True # led off


    # if not d7.value:

        # open Chrome and go to gmail
        # led.value = False # led on
        # open_app("Chrome.app")
        # time.sleep(0.5)
        # kbd.send(Keycode.COMMAND, Keycode.D)
        # layout.write('d0 F4')
        # layout.write('d1 F3')
        # layout.write('d2 F2')
        # layout.write('d3 F1')
        # layout.write('d4 F8')
        # layout.write('d5 F7')
        # layout.write('d6 F6')
        # layout.write('d7 F5 ')

        # time.sleep(0.2)
        # kbd.send(Keycode.F2)
        # layout.write('vscode')
        # time.sleep(0.2)
        # kbd.send(Keycode.COMMAND, Keycode.TAB)
        # layout.write('https://mail.google.com')
        # time.sleep(0.5)
        # kbd.send(Keycode.ENTER)
        # time.sleep(0.1)
        # led.value = True # led off

    # if not d1.value:

    # 	# open finder
    # 	led.value = False # led on
    # 	open_app("~")
    #     led.value = True # led off
    #     time.sleep(0.5)  # debounce delay

    # if not d2.value:

    # 	# open terminal
    # 	led.value = False # led on
    # 	open_app("terminal.app")
    #     time.sleep(0.5)  # debounce delay
    #     led.value = True # led off

    # if not d3.value:

    # 	# open notes
    # 	led.value = False # led on
    # 	open_app("notes.app")
    #     time.sleep(0.5)  # debounce delay
    #     led.value = True # led off

    # if not d4.value:

    # 	# open music
    # 	led.value = False # led on
    # 	open_app("Amazon Music.app")
    #     time.sleep(0.5)  # debounce delay
    #     led.value = True # led off

    # if not d5.value:

    # 	# mute video on bluejeans
    # 	led.value = False # led on
    # 	kbd.send(Keycode.V)
    #     time.sleep(0.3)  # debounce delay
    #     led.value = True # led off

    # if not d6.value:

    # 	led.value = False # led on
    # 	open_app("messages.app")
    #     time.sleep(0.3)  # debounce delay
    #     led.value = True # led off

    # if not d7.value:

    # 	# mute audio on bluejeans
    # 	led.value = False # led on
    # 	kbd.send(Keycode.M)
    #     time.sleep(0.3)  # debounce delay
    #     led.value = True # led off
