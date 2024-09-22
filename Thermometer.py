import machine
import time
import dht
from ssd1306 import SSD1306_I2C

d = dht.DHT11(machine.Pin(12))

i2c = machine.SoftI2C(sda=machine.Pin(21), scl=machine.Pin(22))
i2c.scan()
oled = SSD1306_I2C(128, 64, i2c)


while True:
    d.measure()
    temp = d.temperature()
    humi = d.humidity()
    s1 = f"Temperature:{temp}C"
    s2 = f"Humidity:{humi}%"
    oled.fill(0)
    oled.text(s1, 0, 0)
    oled.text(s2, 0, 10)
    oled.show()
    time.sleep(3)