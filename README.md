# Monitor-de-Temperatura-e-Umidade-com-ESP32
Este projeto utiliza um ESP32 conectado a um sensor DHT11 e um display OLED 128x64 para monitorar e exibir em tempo real a temperatura e a umidade do ambiente.
O circuito foi montado em uma protoboard para facilitar os testes.

* Para esse  projeto eu copiei a biblioteca do LCD e coloquei no arquivo ssd1606.py

🧩 Componentes utilizados

🌡️ Sensor de Temperatura e Umidade DHT11

🖥️ Display OLED 128x64 0.96" I2C (Azul e Amarelo)

⚡ ESP32 USB-C CH340G

🔌 Protoboard 400 pontos

Jumpers (fios de conexão)

🔌 Esquema de ligação

DHT11 → (VCC → 3.3V, GND → GND, DATA → GPIO4 do ESP32)

OLED → (VCC → 3.3V, GND → GND, SDA → GPIO21, SCL → GPIO22)

Como usar

Instale o Thonny IDE ou outro editor compatível com MicroPython.

Grave o firmware do MicroPython no ESP32.

Copie o código para o ESP32 (ex.: main.py).

Reinicie o ESP32.

Os dados serão exibidos no display OLED.


![componentes](https://github.com/user-attachments/assets/bd452411-bcce-4025-8fa5-492aef72d716)

![Fluxograma](https://github.com/user-attachments/assets/fc3d4abe-9537-4ebb-af18-af7a09c74f3b)

![WhatsApp Image 2025-09-10 at 01 22 13](https://github.com/user-attachments/assets/66c02c17-1ac6-4ca6-83fa-f2c6209a120f)



