import machine
import utime
import dht

d = dht.DHT11(Pin(15))
file = open("temp.txt", "w")

while True:
    d.measure()
    temperatura = d.temperature() # em °C
    umidade= d.humidity() # em %
    
    temperatura_str="Temp: "+str(temperatura)+" ºC\n"
    umidade_str="Umid: "+str(umidade)+" %\n"
   
    file.write(temperatura_str)
    file.write(umidade_str)
    
    file.flush()
    utime.sleep(10)