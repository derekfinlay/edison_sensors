import time
import pyupm_grove as grove

# Create the relay switch object using GPIO pin 0
relay = grove.GroveRelay(0)

# Close and then open the relay switch 3 times,
# waiting one second each time.  The LED on the relay switch
# will light up when the switch is on (closed).
# The switch will also make a noise between transitions.
for i in range (0,3):
    relay.on()
    if relay.isOn():
        print relay.name(), 'is on'
    time.sleep(1)
    relay.off()
    if relay.isOff():
        print relay.name(), 'is off'
    time.sleep(1)

# Delete the relay switch object
del relay
