from gpiozero import PWMLED
from time import sleep
import math

led = PWMLED(26)
x=0

while True:
    led.value = math.sin(x)
    x = x + 0.05
    if x > 1:
        x=0
    print(led.value)
    sleep(0.1)
#     led.value = 0 # off
#     sleep(1)
#     led.value = 0.5 # half brightness
#     sleep(1)
#     led.value = 1 # full brightness
#     sleep(1)
