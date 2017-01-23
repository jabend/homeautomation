#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import time

#Script to "Press Buttons" on Westinghouse Outlet Remote. Used in conjunction with HABRIDGE

#Using GPIO pins on Pi Zero that are connected to the switch pads on Westinghouse 28064 remote
#The remote controls three outlets on 433M frequency.  Rather than use a 433 transmitter, I simply
#soldered connectors directly to the products remote control and use GPIO commands to "press" the buttons.

#USAGE: ./basic_onoff.py [Outlet#] [0|1]
#  0=OFF
#  1=ON

#Using the command line arguments passed to the script.  Button subracts 1 to allow orginal outlet
#numbers 1,2,3 to be used rather than forcing user to shift to 0,1,2 based on array position.
BUTTON = int(sys.argv[1])-1
STATE = int(sys.argv[2])

#Assign Button Matrix Wires to RaspberryPi Pins using BOARD numbering
#  Other GPIO pins could have been used but these are the ones I chose to keep the
#  Wires on the Pi header all next to each other.
#    SW_1 = 38
#    SW_2 = 35
#    SW_3 = 36
#    SW_4 = 37
#    SW_ON =40
#    SW_OFF =33

SW=[38,35,36,37]
ST=[33,40]
PRESS_TIME = 0.75

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  ##Use board pin numbers

def releaseButtons():
    #Set the OUTPUT pins stay connected for PRESS_TIME seconds.
    time.sleep(PRESS_TIME)

    #Set all of the GPIO Pins to INPUT, which simulates the release of all buttons on remote.
    GPIO.setup(SW[0], GPIO.IN) ## SW1
    GPIO.setup(SW[1], GPIO.IN) ## SW2
    GPIO.setup(SW[2], GPIO.IN) ## SW3
    GPIO.setup(SW[3], GPIO.IN) ## SW4
    GPIO.setup(ST[0], GPIO.IN)  ## Left Ground
    GPIO.setup(ST[1], GPIO.IN)  ## Right Ground

    #wait a bit to let remote settle down and finish sending before allowing another button press.
    time.sleep(0.25)

#Trigger putton press on the remote
GPIO.setup(SW[BUTTON], GPIO.OUT, initial=0)
GPIO.setup(ST[STATE], GPIO.OUT, initial=0)
releaseButtons()

