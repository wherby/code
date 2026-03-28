# https://codeforces.com/gym/102556/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0325/solution/cf102556h.md
# 利用所有因子的乘积必然是N//2倍幂的条件，所有质数因子的2倍的GCD 则一定是 N的倍数
# 为了求出N，则遍历找到倍数， cnt[x]//g * i 则是原数每个质数因子的数量，利用这个数量可以判断是否能刚好等于 i倍 N

import init_setting
from cflibs import *

def main(): 
    m = II()
    
    if m == 1:
        exit(print(1))
    
    cnt = Counter()
    
    for x in range(2, 4 * 10 ** 7):
        while m % x == 0:
            cnt[x] += 1
            m //= x
    
    if m > 1:
        cnt[m] += 1
    
    g = 0
    for x in cnt.values():
        g = math.gcd(g, 2 * x)
    
    for i in range(1, g + 1):
        if g % i == 0:
            
            factor_cnt = 1
            for x in cnt:
                factor_cnt *= 1 + 2 * cnt[x] // g * i
            
            if i * factor_cnt == g:
                ans = 1
                for x in cnt:
                    ans *= pow(x, 2 * cnt[x] // g * i)
                print(ans)
                exit()
    
    print(-1)