# Access to this file : Election Head
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

reader = SimpleMFRC522()

try:
    text = raw_input('Enter data ')
    print('Place your card')
    reader.write(text)
    print('Data written successfully')
finally:
    GPIO.cleanup()
