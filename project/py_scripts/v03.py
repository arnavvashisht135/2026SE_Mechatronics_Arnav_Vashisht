import time
from machine import Pin, PWM
from servo import Servo


# create a PWM servo controller (16 - pin Pico)
servo_pwm = PWM(Pin(16))

# Set the parameters of the servo pulses, more details in the "Documentation" section
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

# create a servo object
my_servo = Servo(
    pwm=servo_pwm, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)


while True:
    # manually set the servo duty time
    my_servo.set_duty(500)
    time.sleep(2)

    my_servo.set_duty(1500)
    time.sleep(2)

    my_servo.stop()
    time.sleep(2)
