import time
import RPi.GPIO as GPIO

motor_af = 37
motor_ab = 33
motor_bf = 36
motor_bb = 32

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor_af,GPIO.OUT)
GPIO.setup(motor_ab,GPIO.OUT)
GPIO.setup(motor_bf,GPIO.OUT)
GPIO.setup(motor_bb,GPIO.OUT)
GPIO.output(motor_af,GPIO.LOW)
GPIO.output(motor_ab,GPIO.LOW)
GPIO.output(motor_bf,GPIO.LOW)
GPIO.output(motor_bb,GPIO.LOW)

try:
    while True:
        GPIO.output(motor_af,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(motor_af,GPIO.LOW)
        GPIO.output(motor_bf,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(motor_af,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(motor_af,GPIO.LOW)
        GPIO.output(motor_bf,GPIO.LOW)
        time.sleep(1)
        GPIO.output(motor_ab,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(motor_ab,GPIO.LOW)
        GPIO.output(motor_bb,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(motor_ab,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(motor_ab,GPIO.LOW)
        GPIO.output(motor_bb,GPIO.LOW)
        time.sleep(1)
finally:
    GPIO.cleanup()

