from gpiozero import LED
from time import sleep

led = LED(18) #GPIO18 como saída


while True:
        led.on()
        print("Led on")
        sleep(1)
        led.off()
        print("Led off")
        sleep(1)
