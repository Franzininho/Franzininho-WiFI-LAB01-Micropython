from machine import I2C, Pin
from bmp180 import BMP180
import time, ssd1306, framebuf

# atribuição de pinos da Franzininho 
i2c = I2C(scl=Pin(9), sda=Pin(8), freq=100000)

# configurando BMP180
bmp180 = BMP180(i2c)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

# configurando display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# criando símbolo para representar graus no display
degree = bytearray([0x00, 0x0e, 0x11, 0x11, 0x0e, 0x00, 0x00, 0x00])
fb = framebuf.FrameBuffer(degree, 8, 8, framebuf.MONO_HLSB)


while True:
    temp = round(bmp180.temperature, 2)
    p = round(bmp180.pressure, 2)
    alt = round(bmp180.altitude, 2)
    
    temperatura_str="Temp:"+str(temp)
    pressao_str="P:"+str(p)+" Pa"
    altitude_str="Alt:"+str(alt)+" m"
    
    #coletando data e hora atual
    current_time = time.localtime()
    formatted_time = "{:02d}/{:02d}/{} {:02d}:{:02d}".format(current_time[2], current_time[1], current_time[0], current_time[3], current_time[4])

    # limpa display
    oled.fill(0)
    
    # exibição no display
    oled.text(formatted_time, 0, 0)
    oled.framebuf.blit(fb, 53, 15)
    oled.text(temperatura_str+ " " + "C", 0, 20)
    oled.text(pressao_str, 0, 35)
    oled.text(altitude_str, 0, 50)

    oled.show()
    time.sleep(60)

