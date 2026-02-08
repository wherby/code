# https://codeforces.com/gym/106351/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0206/solution/cf106351k.md
# 对于GCD和LCM 同时都有限制的问题，枚举LCM的因子会更简单，因为LCM对应的数字的因子相对于GCD的因子会少很多，LCM因子数量和LCM大小是指数关系，而GCD因子数量和GCD大小是线性关系




import init_setting
from cflibs import *
def main(): 
    M = 100000
    factors = [[] for _ in range(M + 1)]
    
    for i in range(1, M + 1):
        for j in range(i, M + 1, i):
            factors[j].append(i)
    
    n, x, y = MII()
    nums = LII()
    
    cnt = [0] * (M + 1)
    for v in nums:
        cnt[v] += 1
    
    ans = 0
    
    for i in range(x, y + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2
        
        l = len(factors[i])
        for j in range(l):
            for k in range(j):
                g = math.gcd(factors[i][j], factors[i][k])
                if g >= x and factors[i][j] * factors[i][k] // g == i:
                    ans += cnt[factors[i][j]] * cnt[factors[i][k]]
    
    print(ans)