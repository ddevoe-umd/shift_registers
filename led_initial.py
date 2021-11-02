import RPi.GPIO as GPIO
import time

# Set up GPIO ports:
GPIO.setmode(GPIO.BCM)
dataPin, latchPin, clockPin = 16, 12, 6
GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial=0)  # start latch & clock low
GPIO.setup(clockPin, GPIO.OUT, initial=0)  

# Test pattern:
pattern = 0b01100110     # pattern for "4"

# Move each bit from the test pattern into the shift register.
# Use a single-bit bit mask to scan through the binary word
# one bit at a time, pinging the clock each time:
mask = 1                                # bit mask
for i in range(8):                      # 8 bits in pattern
  if (pattern & mask == 0): # is masked bit off?
    GPIO.output(dataPin, 1)
  else:
    GPIO.output(dataPin, 0)
  mask = mask << 1            # shift mask bit left for next bit in "four"

  GPIO.output(clockPin,1)   # ping the clock pin to shift register data
  time.sleep(0)
  GPIO.output(clockPin,0)

# Ping the latch pin to send data to the output:
GPIO.output(latchPin, 1)      # ping the latch pin to send register to output
time.sleep(0)
GPIO.output(latchPin, 0)

# Sit in an infinite loop to continue to display the pattern:
try:
  while 1: pass
except:
  GPIO.cleanup()  # cleanup can ping latch, so only do this at end of code
