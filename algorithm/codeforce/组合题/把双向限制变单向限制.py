# https://codeforces.com/gym/105500/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0418/solution/cf105500i.md
# 把双向限制的组合问题变成单向限制的插槽问题， 从小到大的时候，放入N个物品，就会需要对应N个大1，或者小1 的物品插入，这时从小到大计算物品，就变成了物品插槽匹配问题
# 

import init_setting
from cflibs import *
from lib.combineWithPreCompute import Factorial
def main():
    n = II()
    nums = LII()
    
    M = 10 ** 6 + 5
    mod = 998244353
    
    f = Factorial(n, mod)
    
    cnt = [0] * M
    for x in nums:
        cnt[x] += 1
    
    mi = min(nums)
    ma = max(nums)
    
    ans = f.fac(cnt[mi])
    neighbors = cnt[mi]
    
    for i in range(mi + 1, ma + 1):
        if cnt[i] < neighbors:
            ans = 0
            break
        
        ans = ans * f.fac(cnt[i]) % mod
        ans = ans * f.combi(cnt[i] - 1, neighbors - 1) % mod
        
        neighbors = cnt[i] - neighbors
    
    if neighbors == 0: print(ans * n % mod * f.inv(cnt[mi]) % mod)
    else: print(0)