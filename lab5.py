from gpiozero import Button # importmodule LED
from gpiozero import LED # import module LED
from time import sleep
button = Button(21)
led =LED(26)

while True:
    if button.is_pressed:
        print("Pressed")
        led.on() # set the GPIO 17 to high
    else:
        print("Released")
    led.off() # set the GPIO 17 to low
    sleep(1)