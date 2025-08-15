from machine import Pin, PWM
from servo import Servo
from movement import Movement
from time import sleep

frequency = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))

