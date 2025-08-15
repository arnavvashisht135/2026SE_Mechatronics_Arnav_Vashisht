from victim_sensor import Victim_Sensor
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms
from time import sleep

sensor = PiicoDev_VEML6040()
display = create_PiicoDev_SSD1306()

Victim_Sensor = Victim_Sensor(display, sensor, False)

while True:
    print(Victim_Sensor.SenseVictim())
    sleep(0.1)