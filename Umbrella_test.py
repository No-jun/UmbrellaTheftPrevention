
from m5stack import *
from m5ui import *
from uiflow import *
import urequests
import imu
import time

setScreenColor(0x222222)


imu0 = imu.IMU()

def buttonB_wasPressed():
  # global params
  pass
btnB.wasPressed(buttonB_wasPressed)

setScreenColor(0xffcc00)
while True:
  if (imu0.acceleration[0]) > 1000:
    speaker.tone(800, 0.3)
    try:
      req = urequests.request(method='POST', url='https://maker.ifttt.com/trigger/Linetest/with/key/dNKqpKxg1GOf-MekuoXCv6',json={'value1':'From Your Device!!'}, headers={})
      setScreenColor(0x33cc00)
    except:
      setScreenColor(0xff0000)
    wait(1)
    setScreenColor(0xffcc00)
  else:
    pass
  wait_ms(2)