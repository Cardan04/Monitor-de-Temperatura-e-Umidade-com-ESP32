# ssd1306.py - driver SSD1306 I2C para MicroPython (ESP32/ESP8266)
import framebuf

class SSD1306_I2C:
    def __init__(self, width, height, i2c, addr=0x3c):
        self.width = width
        self.height = height
        self.i2c = i2c
        self.addr = addr
        self.pages = self.height // 8
        self.buffer = bytearray(self.width * self.pages)
        self.framebuf = framebuf.FrameBuffer(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.init_display()

    def init_display(self):
        for cmd in (
            0xae, 0xa4, 0xd5, 0x80,
            0xa8, self.height - 1,
            0xd3, 0x00, 0x40,
            0x8d, 0x14,
            0x20, 0x00,
            0xa1, 0xc8,
            0xda, 0x12,
            0x81, 0xcf,
            0xd9, 0xf1,
            0xdb, 0x40,
            0xa6, 0xaf):
            self.write_cmd(cmd)

    def write_cmd(self, cmd):
        self.i2c.writeto(self.addr, b'\x00' + bytearray([cmd]))

    def write_data(self, buf):
        self.i2c.writeto(self.addr, b'\x40' + buf)

    def show(self):
        for page in range(self.pages):
            self.write_cmd(0xb0 + page)
            self.write_cmd(0x00)
            self.write_cmd(0x10)
            start = self.width * page
            end = start + self.width
            self.write_data(self.buffer[start:end])

    def fill(self, col):
        self.framebuf.fill(col)

    def text(self, string, x, y, col=1):
        self.framebuf.text(string, x, y, col)



