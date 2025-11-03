from gpiozero import LED
from time import sleep

led = LED(18) #GPIO18 como saída


while True: #Cria o Loop Infinito
        led.on() #Liga o LED
        print("Led on") #Mostra na tela que o LED está acesso
        sleep(1) #Aguarda 1 segundo
        led.off() #Desliga o LED
        print("Led off") #Mostra na tela que o LED está apagado
        sleep(1) #Espera 1 segundo
