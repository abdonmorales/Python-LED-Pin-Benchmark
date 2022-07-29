############# Start of Header ############

print("PROGRAM NAME: LED PROTOTYPE BENCHMARK")

red_pin = 20
yellow_pin = 21
green_pin = 23
gpio_pin = 12

import RPi.GPIO as GPIO
import time

for pin in range(12,24):
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin,GPIO.LOW)



############# End of Header #############
####### Start of the test program #######
print("Test has started on prototype")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(gpio_pin,GPIO.LOW)
time.sleep(2)
GPIO.output(gpio_pin,GPIO.HIGH)
time.sleep(2)
GPIO.output(gpio_pin,GPIO.LOW)
time.sleep(2)

print("Test is completed on prototype")

######## End of the test program ######
######## Start of program #############

for pin in range(12, 24):
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, GPIO.LOW)

print("Start of the program for 'The LED 4000 PROTOTYPE'")

for pin in range(12,24):
    GPIO.output(pin,GPIO.LOW)

for i in range(5):
    for pin in range(12,24): # Using pins 16-21
        GPIO.output(red_pin,GPIO.HIGH)
        GPIO.output(yellow_pin,GPIO.HIGH)
        GPIO.output(green_pin,GPIO.HIGH)
        GPIO.output(gpio_pin,GPIO.HIGH)
print("Program finished!")
time.sleep(2)
for pin in range(12,24):
    GPIO.output(pin,GPIO.LOW)