# 计算combination mod 30 用 exLucas  https://chat.deepseek.com/a/chat/s/b854920f-30f6-4706-9cb2-c7f1940038e4

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

def crt(a1, m1, a2, m2, a3, m3):
    # 解方程 x ≡ a1 mod m1, x ≡ a2 mod m2, x ≡ a3 mod m3
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        else:
            g, x, y = extended_gcd(b, a % b)
            return g, y, x - (a // b) * y
    
    # 合并前两个方程
    g, x, y = extended_gcd(m1, m2)
    if (a1 - a2) % g != 0:
        return None  # 无解
    lcm12 = m1 // g * m2
    res12 = (a2 - a1) // g * x % (m2 // g) * m1 + a1
    res12 %= lcm12
    
    # 合并第三个方程
    g, x, y = extended_gcd(lcm12, m3)
    if (res12 - a3) % g != 0:
        return None  # 无解
    lcm123 = lcm12 // g * m3
    res123 = (a3 - res12) // g * x % (m3 // g) * lcm12 + res12
    return res123 % lcm123

def combination_mod_30_exlucas(n, k):
    # 分别计算 C(n, k) mod 2, mod 3, mod 5
    c2 = comb_mod_p(n, k, 2)
    c3 = comb_mod_p(n, k, 3)
    c5 = comb_mod_p(n, k, 5)
    
    # 使用中国剩余定理合并结果
    return crt(c2, 2, c3, 3, c5, 5)
import math

print(combination_mod_30_exlucas(1000,500))
print(math.comb(1000,500)%30)
for i in range(1000):
    a= combination_mod_30_exlucas(1001,i)
    b = math.comb(1001,i) %30
    if a !=b:
        print(a,b,i)