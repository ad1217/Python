#mame-cabinet-joystick.py by Adam Goldsmith 2015-05-11
#based on rpi-gpio-jstk.py by Chris Swan 9 Aug 2012
#using python-uinput

import uinput
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

#Keymap
#List Stricture: uinput name, value when pressed, value when released
keymap = {7:  [uinput.BTN_JOYSTICK, 1,   0],   #Button 1
          11: [uinput.ABS_Y,        0,   128], #Up
          13: [uinput.ABS_Y,        255, 128], #Down
          15: [uinput.ABS_X,        0,   128], #Left
          13: [uinput.ABS_X,        255, 128]} #Right

#Second dictionary to store state
isPressed = {}

# initialize keys
for pin in keymap.keys():
  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  isPressed[pin] = False

events = (uinput.BTN_JOYSTICK, uinput.ABS_X + (0, 255, 0, 0), uinput.ABS_Y + (0, 255, 0, 0))

device = uinput.Device(events)

# Center joystick
# syn=False to emit an "atomic" (128, 128) event.
#device.emit(uinput.ABS_X, 128, syn=False)
#device.emit(uinput.ABS_Y, 128)

while True:
  for pin, value in keymap.items():
    if (not isPressed[pin]) and (not GPIO.input(pin)):
      isPressed[pin] = True
      device.emit(value[0], value[1])
    if isPressed[pin] and GPIO.input(pin):
      isPressed[pin] = False
      device.emit(value[0], value[2]) 
  time.sleep(.02)  # Poll every 20ms (otherwise CPU load gets too high)
