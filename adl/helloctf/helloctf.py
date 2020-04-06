from pwn import *

ip = "ctf.adl.tw"
port = 11001
r = remote(ip, port)
r.interactive()