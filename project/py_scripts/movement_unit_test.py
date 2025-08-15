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

left_servo = Servo(pwm=servo_pwm_left, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

right_servo = Servo(pwm=servo_pwm_right, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

movement = Movement(right_servo, left_servo, False)

print(isinstance(movement, Movement))

print("Forward in 2 seconds")
sleep(2)
movement.move_forward()
print("Backward in 2 seconds")
sleep(2)
movement.move_backward()
print("Stopping in 2 seconds")
sleep(2)
movement.stop()
print("Turning right in 2 seconds")
sleep(2)
movement.rotate_right()
print("Turning left in 2 seconds")
sleep(2)
movement.rotate_left()
print("Stopping in 2 seconds")
sleep(2)
movement.stop()