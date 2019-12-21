import binascii

def string_to_int(string):
    byte = string.encode()               # string to byte
    hexadecimal = binascii.hexlify(byte) # byte to hex
    decimal = int(hexadecimal, 16)       # hex to dec
    return decimal

def int_to_string(int):
    hexadecimal = hex(int)               # dec to hex
    byte = hexadecimal[2:].encode()      # hex to byte (type)
    byte = binascii.unhexlify(byte)      # hex to byte (coding)
    string = byte.decode('utf-8')        # byte to utf-8
    return string