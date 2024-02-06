from machine import Pin
import utime

#setando as cores do led RGB
ledB=Pin(12,Pin.OUT)
ledG=Pin(13,Pin.OUT)
ledR=Pin(14,Pin.OUT)

#configurando botões
botao1= Pin(7,Pin.IN,Pin.PULL_UP)
botao2= Pin(6,Pin.IN,Pin.PULL_UP)
botao3= Pin(5,Pin.IN,Pin.PULL_UP)

#loop para 
while True:
    ledB.value(not botao1.value())
    utime.sleep_ms(100)
    ledG.value(not botao2.value())
    utime.sleep_ms(100)
    ledR.value(not botao3.value())
    utime.sleep_ms(100)