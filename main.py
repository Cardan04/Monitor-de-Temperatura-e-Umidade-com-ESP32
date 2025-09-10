from machine import Pin, I2C
import ssd1306
import dht
import time

# Configurações do I2C para o OLED
i2c = I2C(0, scl=Pin(18), sda=Pin(21))  # GPIO18 = SCL, GPIO21 = SDA
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Configurações do DHT11
sensor = dht.DHT11(Pin(23))  # Pino GPI23

while True:
    try:
        # Faz a leitura
        sensor.measure()
        temp = sensor.temperature()
        umid = sensor.humidity()

        # Exibe no console
        print("Temperatura:", temp, "°C")
        print("Umidade:", umid, "%")

        # Exibe no OLED
        oled.fill(0)  # limpa tela
        oled.text("Temp: {} C".format(temp), 0, 0)
        oled.text("Umid: {} %".format(umid), 0, 16)
        oled.show()

    except Exception as e:
        oled.text("Erro na leitura:", e)

    time.sleep(2)  # aguarda 2 segundos

