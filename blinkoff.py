#!/usr/bin/env python3

from gpiozero import LED
import time

led = LED(18) #GPIO18 como saída

led.off() #Desliga o LED
#Mostra na tela se realemnte desligou
print("Serviço de Blink parado, LED desligado.")
