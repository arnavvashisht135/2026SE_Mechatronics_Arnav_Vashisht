from machine import Pin, PWM
from servo import Servo

freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))

left_servo = Servo(pwm=servo_pwm_left, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

right_servo = Servo(pwm=servo_pwm_right, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

class Movement:
    def __init__(self, right_servo, left_servo, debug=True):
        self.__right_servo = right_servo
        self.__left_servo = left_servo
        self.__debug = debug

    def move_forward(self):
        if self.__debug:
            print("Moving Forward")
        self.__right_servo.set_duty(1000)
        self.__left_servo.set_duty(2000)

    def move_backward(self):
        if self.__debug:
            print("Moving Backwards")
        self.__right_servo.set_duty(2000)
        self.__left_servo.set_duty(1000)

    def rotate_right(self):
        if self.__debug:
            print("Turning Right")
        self.__right_servo.set_duty(1500)
        self.__left_servo.set_duty(2000)

    def rotate_left(self):
        if self.__debug:
            print("Turning Left")
        self.__right_servo.set_duty(1000)
        self.__left_servo.set_duty(1500)

    def stop(self):
        if self.__debug:
            print("Stop")
        self.__right_servo.stop()
        self.__left_servo.stop()