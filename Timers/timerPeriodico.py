from machine import Pin, Timer
import utime

ledR= Pin(14,Pin.OUT) #definindo o pino 14 como saída
temporizador = Timer(0) #definindo timer

ledState = False

def toogleLed ():
    global ledState
    ledState = not ledState
    ledR.value(ledState)

def tempo (timer): #definindo função callback
    global ledR
    toogleLed() # muda estado do led

temporizador.init(period = 1000, mode = Timer.PERIODIC, callback = tempo)
# configurando timer com frequência de 1Hz e no modo periódico