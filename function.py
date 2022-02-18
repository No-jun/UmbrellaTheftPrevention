# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# 鍵をかけるようにモータを回転
def lock():
    servo_pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gp_out, GPIO.OUT)
    servo = GPIO.PWM(gp_out, 50)
    servo.start(0.0)
    servo.ChangeDutyCycle(15.0)
    time.sleep(0.5)
    GPIO.cleanup()


# 鍵をあけるようにモータを回転
def unlock():
    servo_pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gp_out, GPIO.OUT)
    servo = GPIO.PWM(gp_out, 50)
    servo.start(0.0)
    servo.ChangeDutyCycle(5.5)
    time.sleep(0.5)
    GPIO.cleanup()