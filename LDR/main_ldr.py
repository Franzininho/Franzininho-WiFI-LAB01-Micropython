import machine
import utime

led_red= machine.Pin(14,machine.Pin.OUT) #definindo o pino 16 como saída digital
ldr= machine.ADC(machine.Pin(1)) #definindo entrada analógica

fator_conversao = 3.3 / (65535)

while True:
    leitura_LDR = ldr.read_u16() * fator_conversao
    utime.sleep(1)
    print(leitura_LDR)
    if (leitura_LDR < 1):
       led_red.value(1)
    else:
        led_red.value(0)