#!/usr/bin/python

import mraa
import time
import fcntl
import struct
import pyupm_i2clcd as lcd

color = ['255, 255, 0', '0, 255, 0', '255, 0, 0']


# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

# Clear
myLcd.clear()
time.sleep( 1 )
# Green
myLcd.setColor(255, 255, 0)
time.sleep( 1 )
# Zero the cursor
myLcd.setCursor(0,0)
time.sleep( 1 )
myLcd.write('....waiting....')

BUTTON_GPIO = 6                # The button GPIO
ledState = False               # LED is off to begin with

btn = mraa.Gpio(BUTTON_GPIO)
btn.dir(mraa.DIR_IN)
  
def getButtonPress():
    while 1:
        if (btn.read() != 0):
            continue
        else:
            time.sleep(0.05)
            if (btn.read() == 1):
                return
            else:
                continue

color_now =  color[1]
while 1:
        getButtonPress()
        if ledState == True:
            myLcd.clear()
            myLcd.setColor(0, 255, 0)
            myLcd.setCursor(0,0)
            myLcd.write('off')
            ledState = False
        else:
           myLcd.clear()
           myLcd.setColor(0, 255, 255)
           myLcd.setCursor(1,0)
           myLcd.write('on')            
           ledState = True

        time.sleep(0.005)
