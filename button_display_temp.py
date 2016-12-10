#!/usr/local/bin/python

import pyupm_i2clcd as lcd
import mraa
import time
import sys
import math

tmpPin=2
tmp = mraa.Aio(tmpPin)
tmpVal = 0

# digital input - touch
touchPin = mraa.Gpio(3)
touchPin.dir(mraa.DIR_IN)

# display - lcd
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)

tmp1Val = float(tmp.read())
bVal = 3975
lumStr = "Temp: "+str(tmp1Val)
lcdDisplay.setCursor(1, 0)
lcdDisplay.write(lumStr)
time.sleep(30)
lcdDisplay.setCursor(1, 0)
lcdDisplay.write("            ***              ")
