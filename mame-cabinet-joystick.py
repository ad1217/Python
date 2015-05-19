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

CharliePins = ([])

# initialize keys
for pin in keymap.keys():
  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  isPressed[pin] = False

for pins in CharlieMap:
  CharliePins =CharliePins.update(pins)
  for pin in pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    isPressed[pin] = False

def checkPressed (state, key, value):
  value[0].emit(value[1], value[2])
  if (not isPressed[key]) and state:
    isPressed[key] = True
    value[0].emit(value[1], value[2])
  if isPressed[key] and (not state):
    isPressed[key] = False
    value[0].emit(value[1], value[3])

while True:
  for key, value in keymap.items():
    checkPressed((not GPIO.input(key)), key, value)

  for key, value in CharlieMap.items():
    for pin in CharliePins:
      GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(key[0], GPIO.OUT)
    GPIO.output(key[0], GPIO.HIGH
    checkPressed(GPIO.input(key[1]), key, value):
  time.sleep(.01)  # Poll every 10ms (otherwise CPU load gets too high)
