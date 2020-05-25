import binascii

f = open("pika.png", "rb")

for i in f:
    print(i)
    # print(binascii.b2a_hex(i))