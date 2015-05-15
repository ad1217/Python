#!/usr/bin/python
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pins=[5,7,8,11,12,13,15,16,18,19,21,22,23,24,26,29,31,32,33,37,38,40]

buttons =["[device1, uinput.ABS_Y, 0,   128], #Up",
          "[device1, uinput.ABS_Y, 255, 128], #Down",
          "[device1, uinput.ABS_X, 0,   128], #Left",
          "[device1, uinput.ABS_X, 255, 128], #Right",
          "[device1, uinput.BTN_0, 1,   0],   #Button 1",
          "[device1, uinput.BTN_1, 1,   0],   #Button 2",
          "[device1, uinput.BTN_2, 1,   0],   #Button 3",
          "[device1, uinput.BTN_3, 1,   0],   #Button 4",
          "[device1, uinput.BTN_4, 1,   0],   #Button 5",
          "[device1, uinput.BTN_5, 1,   0],   #Button 6",
          "[device2, uinput.ABS_Y, 0,   128], #Up",
          "[device2, uinput.ABS_Y, 255, 128], #Down",
          "[device2, uinput.ABS_X, 0,   128], #Left",
          "[device2, uinput.ABS_X, 255, 128], #Right",
          "[device2, uinput.BTN_0, 1,   0],   #Button 1",
          "[device2, uinput.BTN_1, 1,   0],   #Button 2",
          "[device2, uinput.BTN_2, 1,   0],   #Button 3",
          "[device2, uinput.BTN_3, 1,   0],   #Button 4",
          "[device2, uinput.BTN_4, 1,   0],   #Button 5",
          "[device2, uinput.BTN_5, 1,   0],   #Button 6",
          "[device1, uinput.BTN_6, 1,   0],   #1p Start",
          "[device1, uinput.BTN_7, 1,   0],   #2p Start",
          "[device1, uinput.BTN_8, 1,   0],   #1p coin",
          "[device1, uinput.BTN_9, 1,   0]}   #2p coin"]

file=open("config.py", "w")
file.write("import uinput\n#Keymap\n#List Stricture: uinput name, value when pressed, value when released\n")
file.write("events = (uinput.BTN_0, uinput.BTN_1, uinput.BTN_2, uinput.BTN_3, uinput.BTN_4, uinput.BTN_5, uinput.BTN_6, uinput.BTN_7, uinput.BTN_8, uinput.BTN_9, uinput.ABS_X + (0, 255, 0, 0), uinput.ABS_Y + (0, 255, 0, 0))\ndevice1 = uinput.Device(events)\ndevice2 = uinput.Device(events)\n")
file.write("keymap={")

for i in pins:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for button in buttons:
    print button
    done = False
    while not done:
        for i in pins:
            if (not GPIO.input(i)):
                print(i)
                file.write(str(i) + ": " + button + "\n")
                while not GPIO.input(i):
                    time.sleep(.01)
                done = True
                break
            time.sleep(.01)

file.close()
