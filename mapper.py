#!/usr/bin/python
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pins=[7,8,11,12,13,15,16,18,19,21,22,23,24,26,29,31,32,33,37,38]

buttons=["Up","Down","Left","Right","1","2","3","4","5","6"]

file=open("outfile.txt", "w")

for i in pins:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for button in buttons:
    print button
    done = False
    while not done:
        for i in pins:
            if (not GPIO.input(i)):
                print(i)
                file.write(str(i) + "\n")
                while not GPIO.input(i):
                    time.sleep(.01)
                done = True
                break
            time.sleep(.01)
