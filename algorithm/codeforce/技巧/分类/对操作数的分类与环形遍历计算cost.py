# https://codeforces.com/gym/105803/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0123/solution/cf105803c.md
# 操作数k的分类和环形cost遍历计算


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, k = MII()
        nums = LII()
        
        if k != n - 1:
            outs.append((-sum(nums)) % n)
        else:
            cnt = [0] * n
            for x in nums:
                cnt[(-x) % n] += 1
            
            cur = sum(i * cnt[i] for i in range(n))
            ans = cur
            
            for i in range(n):
                cur += n * cnt[i]
                cur -= n
                ans = fmin(ans, cur)
            
            outs.append(ans)
    
    print('\n'.join(map(str, outs)))