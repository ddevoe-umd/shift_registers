import time
from led_display import LEDdisplay

# Note that we don't need RPi.GPIO here since all the I/O
# is done through the LEDdisplay class (we do however need
# to define the GPIO pins here, since LEDdisplay is
# pin-agnostic)

dataPin, latchPin, clockPin = 16, 12, 6

# Pick a number sequence
sequence = [8, 6, 7, 5, 3, 0, 9];

theLEDdisplay= LEDdisplay(dataPin, latchPin, clockPin)

while True:
  for n in range(len(sequence)):
    theLEDdisplay.setNumber(sequence[n])
    time.sleep(0.4)
