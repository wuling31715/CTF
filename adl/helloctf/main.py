from pwn import *
import struct

print(cyclic(100))
ip = 'ctf.adl.tw'
port = 11001
r = remote(ip, port)
r.interactive()

