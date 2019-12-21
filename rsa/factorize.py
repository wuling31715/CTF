import sympy as sp

def factorize(x):
    is_prime = True
    for i in sp.primerange(0, x ** 0.5 + 1):
        if x % i == 0:
            j = x // i
            is_prime = False
            return [i, j]
    if is_prime:
        return [0, x]

def factorize2(x):
    fact_list = list()
    if sp.isprime(x) == False:
        fact = 1
        while fact != 0:
            fact, x = factorize(x)    
            if fact != 0:
                fact_list.append(fact)
        if x != 1:
            fact_list.append(x)
    else:
        fact_list.append(x)
    return fact_list
