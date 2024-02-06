from machine import Pin, Timer

ledR= Pin(14,Pin.OUT) #definindo o pino 14 como saída
temporizador = Timer(0) 

def desliga (timer): #definindo função callback
    global ledR
    ledR.off()
    print("led desligado")

print("Iniciando o timer")
temporizador.init(period = 3000, mode = Timer.ONE_SHOT, callback = desliga)
ledR.on()