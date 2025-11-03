#!/usr/bin/env python3

from gpiozero import LED
import time

led = LED(18) #GPIO18 como saída

led.off()
# Apenas para fins de log, para sabermos que ele executou
print("Serviço de Blink parado, LED desligado.")
