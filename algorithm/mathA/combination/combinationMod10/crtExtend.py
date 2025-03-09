# 中国剩余定理合并结果

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y
    
def crt(primes, remainders):
    if not primes or not remainders or len(primes) != len(remainders):
        raise ValueError("Input lists must be non-empty and of equal length.")
    
    # 初始化结果为第一个同余方程的解
    x = remainders[0]
    m = primes[0]
    
    # 逐步合并剩余的同余方程
    for i in range(1, len(primes)):
        a_i = remainders[i]
        p_i = primes[i]
        
        # 解方程 x + t * m ≡ a_i mod p_i
        g, t, _ = extended_gcd(m, p_i)
        if (a_i - x) % g != 0:
            return None  # 无解
        
        # 更新结果
        lcm = m // g * p_i
        x = x + (a_i - x) // g * t % (p_i // g) * m
        x %= lcm
        
        # 更新模数
        m = lcm
    
    return x


# Test

def comb_mod_p(n, k, p):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    # 预计算阶乘和逆元
    fact = [1] * (p + 1)
    for i in range(1, p + 1):
        fact[i] = fact[i - 1] * i % p
    
    def lucas(n, k, p):
        res = 1
        while n > 0 or k > 0:
            n_mod = n % p
            k_mod = k % p
            if k_mod > n_mod:
                return 0
            res = res * fact[n_mod] * pow(fact[k_mod] * fact[n_mod - k_mod], p - 2, p) % p
            n //= p
            k //= p
        return res
    
    return lucas(n, k, p)


def combination_mod_30_exlucas(n, k):
    # 分别计算 C(n, k) mod 2, mod 3, mod 5
    c2 = comb_mod_p(n, k, 2)
    c3 = comb_mod_p(n, k, 3)
    c5 = comb_mod_p(n, k, 5)
    c7 = comb_mod_p(n, k, 7)
    
    # 使用中国剩余定理合并结果
    return crt([2,3,5,7],[c2,c3,c5,c7])
import math

for i in range(1000):
    a= combination_mod_30_exlucas(5001,i)
    b = math.comb(5001,i) %210
    if a !=b:
        print(a,b,i)