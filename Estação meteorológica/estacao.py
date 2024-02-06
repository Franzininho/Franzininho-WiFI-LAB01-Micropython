from machine import Pin, SoftI2C
from bmp180 import BMP180
import ssd1306, dht, framebuf, time

# atribuição de pinos da Franzininho 
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))

# configurando display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# criando simbolo para representar graus no display
degree = bytearray([0x00, 0x0e, 0x11, 0x11, 0x0e, 0x00, 0x00, 0x00])
fb = framebuf.FrameBuffer(degree, 8, 8, framebuf.MONO_HLSB)

#configurando sensor de chuva
sensor_chuva= Pin(2, Pin.IN)

# configurando DHT
d = dht.DHT11(Pin(15))

# configurando BMP180
bmp180 = BMP180(i2c)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

# configurando pino do MQ135
mq135= Pin(5,Pin.IN)

while True:
    # coletando dados de umidade e temperatura
    d.measure()
    temperatura = d.temperature() # em °C
    umidade= d.humidity() # em % 

    temperatura_str="Temp: "+str(temperatura)
    umidade_str="Umid: "+str(umidade)+" %"
    
    #coletando pressão e altitude
    p = round(bmp180.pressure, 2)
    alt = round(bmp180.altitude, 2)
    
    pressao_str="P:"+str(p)+" Pa"
    altitude_str="Alt:"+str(alt)+" m"
    
    #coletando data e hora atual
    current_time = time.localtime()
    formatted_time = "{:02d}/{:02d}/{} {:02d}:{:02d}".format(current_time[2], current_time[1], current_time[0], current_time[3], current_time[4])
    print(formatted_time)

    # limpa display
    oled.fill(0)
    
    # exibição no display
    oled.text(umidade_str, 0, 0)
    oled.framebuf.blit(fb, 63, 8)
    oled.text(temperatura_str+ " " + "C", 0, 10)
    
    oled.text(pressao_str, 0, 20)
    oled.text(altitude_str, 0, 30)
    if sensor_chuva.value():
        oled.text("Chuva: Ausente", 0, 40)
    else:
        oled.text("Chuva: Detectado", 0, 40)
        
    if mq135.value() == 1:
        oled.text("Odor: Ausente", 0, 50)

    else:
        oled.text("Odor: Detectado", 0, 50)
        
    oled.show()
    time.sleep(10)
    


