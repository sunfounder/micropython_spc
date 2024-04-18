from machine import I2C as mpI2C

class I2C():
    def __init__(self, address=None, bus=None, sda=None, scl=None):
        self._address = address
        self._bus = mpI2C(bus, sda=sda, scl=scl)

    def set_address(self, address):
        self._address = address

    def write_byte(self, data):
        self._bus.writeto(self._address, bytearray([data]))

    def write_byte_data(self, reg, data):
        self._bus.writeto_mem(self._address, reg, bytearray([data]))

    def write_word_data(self, reg, data):
        self._bus.writeto_mem(self._address, reg, bytearray([data >> 8, data & 0xFF]))

    def write_block_data(self, reg, data):
        self._bus.writeto_mem(self._address, reg, bytearray(data))

    def read_byte(self):
        return self._bus.readfrom(self._address, 1)[0]

    def read_byte_data(self, reg):
        return self._bus.readfrom_mem(self._address, reg, 1)[0]

    def read_word_data(self, reg):
        data = self._bus.readfrom_mem(self._address, reg, 2)
        return (data[1] << 8) | data[0]

    def read_block_data(self, reg, num):
        return self._bus.readfrom_mem(self._address, reg, num)

    def is_ready(self):
        addresses = self._bus.scan()
        if self._address in addresses:
            return True
        else:
            return False

    def scan(self):
        return self._bus.scan()