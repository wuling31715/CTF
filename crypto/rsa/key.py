import sympy as sp
import random
import euler
import factorize
import gcd as GCD

def generate_key():
    public_key, private_key = 0, 0
    prime = list(sp.primerange((10 ** 3), (10 ** 4)))   
    while (public_key == 0) or (private_key == 0):      
        p, q = random.choices(prime, k=2)               # 隨機生成兩質數p, q 
        n = p * q                                       # n = p * q
        o = euler.euler_function(p, q)                        # 歐拉函數
        public_key, private_key = factorize.factorize(o * 10 + 1) # 生成公鑰、私鑰
        gcd = GCD.greatest_common_divisor(public_key, o)
        remainder = public_key * private_key % o
        print('gcd: %i' % gcd)
        print('remainder: %i' % remainder)
        if gcd == 1 and remainder == 1:                 # 檢查是否互質
            print('generate key success\n')
            break
        else:
            print('generate key fail\n')
    return p, q, public_key, private_key, n