# LEDdisplay class
# Extends Shifter class to use shift register for control

import time
import random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

from shifter import Shifter

class LEDdisplay():

  numbers = [ 
    0b11111100, # 0
    0b01100000, # 1
    0b11011010, # 2
    0b11110010, # 3
    0b01100110, # 4
    0b10110110, # 5
    0b10111110, # 6
    0b11100000, # 7
    0b11111110, # 8
    0b11100110] # 9

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)

  def setNumber(self, num):  # display a given number
    self.shifter.shiftByte(~LEDdisplay.numbers[num])
    self.shifter.ping(self.shifter.latchPin)

  def setSinglePin(self, pinNum):
    # new method to allow a single pin to be set high
    # with all other register output pins low
    for i in range(1,9):
      state = 0 if i == pinNum else 1
      GPIO.output(self.shifter.dataPin, state)
      self.shifter.ping(self.shifter.clockPin)
    self.shifter.ping(self.shifter.latchPin)

  def randomPins(self):
    for i in range(8):
      GPIO.output(self.shifter.dataPin, random.randint(0,1))
      self.shifter.ping(self.shifter.clockPin)
    self.shifter.ping(self.shifter.latchPin)
