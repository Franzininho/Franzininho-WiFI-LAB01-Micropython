from machine import Pin, SoftI2C
import ssd1306
import framebuf
import images_repo
import utime

# Franzininho Pin assignment 
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))

oled_width = 128 # Largura da tela OLED
oled_height = 64 # Altura da tela OLED
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    for image in images_repo.images_list:
        buffer = image

        fb = framebuf.FrameBuffer(buffer, 128, 64, framebuf.MONO_HLSB)
        oled.framebuf.fill(0)
        oled.framebuf.blit(fb, 8, 0)

        oled.show()
        utime.sleep_ms(2000)