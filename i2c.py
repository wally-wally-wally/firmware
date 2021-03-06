import smbus

MAIN_CHANNEL = 1

class I2C():
    # Channel: I2C channel; 0 or 1
    def __init__(self, channel):
        self.bus = smbus.SMBus(channel)

    # Addr: Address, Reg: Register, val: array of 32 bit values to write
    def write(self, addr, reg, val):
        self.bus.write_block_data(addr, reg, val)

    # Writes a 16 bit word; used by encoders
    def write_word(self, addr, val):
        self.bus.write_word(addr, val)

    # Writes a byte directly without sending the register value; used by mux
    def write_byte(self, addr, val):
        self.bus.write_byte(addr, val)

    # Reads a byte directly without sending the register value; used by mux
    def read_byte(self, addr, val):
        return self.bus.read_byte(addr, val)

    def read(self, addr, reg):
        return self.bus.read_block_data(addr, reg)

    # Reads 16 bit word; used by encoders
    def read_word(self, addr, reg):
        return self.bus.read_word_data(addr, reg)

