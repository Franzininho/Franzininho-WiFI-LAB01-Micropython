from machine import Pin, PWM
import utime

# Configuração dos pinos para o LED RGB
ledR = 14  # Pino para o LED vermelho
ledG = 13  # Pino para o LED verde
ledB = 12  # Pino para o LED azul

# Configuração dos objetos PWM para controle de intensidade
pwm_red = PWM(Pin(ledR), freq=500)
pwm_green = PWM(Pin(ledG), freq=500)
pwm_blue = PWM(Pin(ledB), freq=500)

def set_color(red, green, blue):
    # Configura a intensidade para cada cor
    pwm_red.duty(int(red * 1023 / 255))
    pwm_green.duty(int(green * 1023 / 255))
    pwm_blue.duty(int(blue * 1023 / 255))

# Semáforo
while True:
    set_color(255, 0, 0)  # Vermelho
    utime.sleep(5)
    set_color(0, 255, 0)  # Verde
    utime.sleep(5)
    set_color(255, 60, 0)  # Amarelo
    utime.sleep(3)
 