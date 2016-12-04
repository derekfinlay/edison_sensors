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

while 1:
    while touchPin.read() == 1:
        # turn led on
        time.sleep(3)
        tmp1Val = float(tmp.read())
        bVal = 3975
        resistanceVal = (1023 - tmp1Val) * 10000 / tmp1Val
        celsiusVal = 1 / (math.log(resistanceVal / 10000) / bVal + 1 / 298.15) - 273.15
        fahrVal = (celsiusVal * (9 / 5)) + 32
        tmpVal = fahrValr)
        lumStr = "Temp: "+str(tmpVal)
        lcdDisplay.setCursor(1, 0)
        lcdDisplay.write(lumStr)
        time.sleep(30)
        lcdDisplay.setCursor(1, 0)
        lcdDisplay.write("            ***              ")
