#mame-cabinet-joystick.py by Adam Goldsmith 2015-05-11
#based on rpi-gpio-jstk.py by Chris Swan 9 Aug 2012
#using python-uinput

import uinput
import time
import RPi.GPIO as GPIO
from config import *

GPIO.setmode(GPIO.BOARD)

#Second dictionary to store state
isPressed = {}

# initialize keys
for pin in keymap.keys():
  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  isPressed[pin] = False

while True:
  for pin, value in keymap.items():
    if (not isPressed[pin]) and (not GPIO.input(pin)):
      isPressed[pin] = True
      value[0].emit(value[1], value[2])
    if isPressed[pin] and GPIO.input(pin):
      isPressed[pin] = False
      value[0].emit(value[1], value[3])
  time.sleep(.01)  # Poll every 10ms (otherwise CPU load gets too high)
