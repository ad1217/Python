#!/usr/bin/python3
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pinMin=1
pinMax=26

buttons=["Up","Down","Left","Right","1","2","3","4","5","6"]

file=open("outfile.txt", "w")

for i in range(pinMin,pinMax):
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Player 1:");
for button in buttons:
    print(button)
    for i in range(pinMin,pinMax):
        if (not GPIO.input(i)):
            print(i)
            file.write(i)
            break
        time.sleep(.02);

file.write('\n')
print("Player 2:");
for button in buttons:
    print(button)
    for i in range(pinMin,pinMax):
        if (not GPIO.input(i)):
            print(i)
            file.write(i)
            break
        time.sleep(.02);
