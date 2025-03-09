# Wrong answer 
# 可能可以使用 algorithm/mathA/combination/combinationMod10/cobinationMod10.py 这里的方法计算
def comb_mod_pk(n, k, p, pk):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    # 计算 n! 中 p 的幂次
    def count_p_in_factorial(n, p):
        count = 0
        while n > 0:
            count += n // p
            n //= p
        return count
    
    # 计算 n! / p^v mod pk，其中 v 是 p 的幂次
    def factorial_mod(n, p, pk):
        res = 1
        while n > 0:
            for i in range(1, pk):
                if i % p != 0:
                    res = res * i % pk
            res = pow(res, n // pk, pk)
            for i in range(1, n % pk + 1):
                if i % p != 0:
                    res = res * i % pk
            n //= p
        return res
    
    # 计算 C(n, k) mod pk
    v = count_p_in_factorial(n, p) - count_p_in_factorial(k, p) - count_p_in_factorial(n - k, p)
    if v >= pk.bit_length():
        return 0  # p^v 超过 pk，结果为 0
    
    num = factorial_mod(n, p, pk)
    denom = factorial_mod(k, p, pk) * factorial_mod(n - k, p, pk) % pk
    return num * pow(denom, pk // p * (p - 1) - 1, pk) % pk * pow(p, v, pk) % pk
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y

def crt(remainders, moduli):
    if not remainders or not moduli or len(remainders) != len(moduli):
        raise ValueError("Input lists must be non-empty and of equal length.")
    
    x = remainders[0]
    m = moduli[0]
    
    for i in range(1, len(moduli)):
        a_i = remainders[i]
        p_i = moduli[i]
        
        g, t, _ = extended_gcd(m, p_i)
        if (a_i - x) % g != 0:
            return None  # 无解
        
        lcm = m // g * p_i
        x = x + (a_i - x) // g * t % (p_i // g) * m
        x %= lcm
        
        m = lcm
    
    return x

def combination_mod_630_exlucas(n, k):
    # 分别计算 C(n, k) mod 2, mod 9, mod 5, mod 7
    c2 = comb_mod_pk(n, k, 2, 2)
    c9 = comb_mod_pk(n, k, 3, 9)
    c5 = comb_mod_pk(n, k, 5, 5)
    c7 = comb_mod_pk(n, k, 7, 7)
    
    # 使用中国剩余定理合并结果
    return crt([c2, c9, c5, c7], [2, 9, 5, 7])

import math

for i in range(1000):
    a= combination_mod_630_exlucas(5001,i)
    b = math.comb(5001,i) %630
    if a !=b:
        print(a,b,i)