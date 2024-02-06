from machine import Pin, SoftI2C
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

# configurando DHT
d = dht.DHT11(Pin(15))

while True:
    # coletando dados de umidade e temperatura
    d.measure()
    temperatura = d.temperature() # em °C
    umidade= d.humidity() # em % 

    temperatura_str="Temp: "+str(temperatura)
    umidade_str="Umid: "+str(umidade)+" %"
    
    #coletando data e hora atual
    current_time = time.localtime()
    formatted_time = "{:02d}/{:02d}/{} {:02d}:{:02d}".format(current_time[2], current_time[1], current_time[0], current_time[3], current_time[4])

    # limpa display
    oled.fill(0)
    
    # exibição no display
    oled.text(formatted_time, 0, 0)
    oled.framebuf.blit(fb, 63, 20)
    oled.text(temperatura_str+ " " + "C", 0, 25)
    oled.text(umidade_str, 0, 40)
    oled.show()
    time.sleep(60)

