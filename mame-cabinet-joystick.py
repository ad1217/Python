#mame-cabinet-joystick.py by Adam Goldsmith 2015-05-11
#based on rpi-gpio-jstk.py by Chris Swan 9 Aug 2012
#using python-uinput

import uinput
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

#Keymap
#List Stricture: uinput name, value when pressed, value when released

events = (uinput.BTN_0, uinput.BTN_1, uinput.BTN_2, uinput.BTN_3, uinput.BTN_4, uinput.BTN_5, uinput.ABS_X + (0, 255, 0, 0), uinput.ABS_Y + (0, 255, 0, 0))

device1 = uinput.Device(events)
device2 = uinput.Device(events)

keymap = {32: [device1, uinput.ABS_Y, 0,   128], #Up
          33: [device1, uinput.ABS_Y, 255, 128], #Down
          31: [device1, uinput.ABS_X, 0,   128], #Left
          26: [device1, uinput.ABS_X, 255, 128], #Right
          7 : [device1, uinput.BTN_0, 1,   0],   #Button 1
          37: [device1, uinput.BTN_1, 1,   0],   #Button 2
          8 : [device1, uinput.BTN_2, 1,   0],   #Button 3
          24: [device1, uinput.BTN_3, 1,   0],   #Button 4
          29: [device1, uinput.BTN_4, 1,   0],   #Button 5
          23: [device1, uinput.BTN_5, 1,   0],   #Button 6
          21: [device2, uinput.ABS_Y, 0,   128], #Up
          11: [device2, uinput.ABS_Y, 255, 128], #Down
          18: [device2, uinput.ABS_X, 0,   128], #Left
          16: [device2, uinput.ABS_X, 255, 128], #Right
          22: [device2, uinput.BTN_0, 1,   0],   #Button 1
          12: [device2, uinput.BTN_1, 1,   0],   #Button 2
          13: [device2, uinput.BTN_2, 1,   0],   #Button 3
          38: [device2, uinput.BTN_3, 1,   0],   #Button 4
          15: [device2, uinput.BTN_4, 1,   0],   #Button 5
          19: [device2, uinput.BTN_5, 1,   0]}   #Button 6

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
  time.sleep(.02)  # Poll every 20ms (otherwise CPU load gets too high)
