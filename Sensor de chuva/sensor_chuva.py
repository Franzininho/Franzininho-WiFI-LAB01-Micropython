from machine import Pin, I2C
import time, ssd1306

#configurando sensor
sensor_chuva= Pin(2, Pin.IN)
led_red = Pin(14, Pin.OUT)

# atribuição de pinos da Franzininho 
i2c = I2C(scl=Pin(9), sda=Pin(8), freq=100000)

# configurando display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)    
while True:
    #coletando data e hora atual
    current_time = time.localtime()
    formatted_time = "{:02d}/{:02d}/{} {:02d}:{:02d}".format(current_time[2], current_time[1], current_time[0], current_time[3], current_time[4])

    # limpa display
    oled.fill(0)
    
    # exibição no display
    oled.text(formatted_time, 0, 0)
    
    if sensor_chuva.value():
        oled.text("Sem chuva", 0, 30)
        led_red.off()
    
    else:
        oled.text("Chovendo", 0, 30)
        led_red.on()
        
    oled.show()
    time.sleep(5)