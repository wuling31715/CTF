import factorize
import gcd
import euler
import transfer
import code
import key
import numpy as np
    
# 測試    
print(factorize.factorize(1024))
print(factorize.factorize2(1024))
print(gcd.greatest_common_divisor(4, 6))
print(euler.euler_function(3, 5))
string = 'Hello World! 你好！'
integer = transfer.string_to_int(string)
print(integer)
message = transfer.int_to_string(integer)
print(message)
print(code.decode2(19, [2 for i in range(100)], 7))

# 金鑰
p, q, public_key, private_key, n = key.generate_key()
private_key_fact_list = factorize.factorize2(private_key)   # 分解 private key
print('p: %i' % p)
print('q: %i' % q)
print('public key: %i' % public_key)
print('private key: %i = %s' % (private_key, str(private_key_fact_list)))
print('n: %i' % n)

# 加密
plaintext = 'Hello World!'
plaintext_list = list()
cyphertext_list = list()
for i in plaintext:
    integer = transfer.string_to_int(i)
    plaintext_list.append(integer)
    cyphertext = code.encode(integer, public_key, n)
    cyphertext_list.append(cyphertext)
print('訊息：%s' % str(plaintext))
print('明文：%s' % str(plaintext_list))
print('密文：%s' % str(cyphertext_list))

# 解密
message = ''
for i in cyphertext_list:
    plaintext = code.decode2(i, private_key_fact_list, n)
    message += transfer.int_to_string(plaintext)
print('密文：%s' % str(cyphertext_list)) 
print('明文：%s' % str(plaintext_list))
print('訊息：%s' % str(message))