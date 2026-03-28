# https://codeforces.com/gym/106433/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0320/solution/cf106433d.md
# 这里可以重排的关键是相邻排序队列互质，所以有相同质因子的不能交换顺序，所以需要查找逆序对

import init_setting
from cflibs import *
def main(): 
    M = 10 ** 6 + 5
    pr = list(range(M))
    
    for i in range(2, M):
        if pr[i] == i:
            for j in range(i, M, i):
                pr[j] = i
    
    def prime_factor(x):
        ans = []
        while x > 1:
            p = pr[x]
            ans.append(p)
            while x % p == 0:
                x //= p
        return ans
    
    t = II()
    outs = []
    
    vis = [0] * M
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        flg = True
        
        for x in nums:
            for p in prime_factor(x):
                if vis[p] > x:
                    flg = False
                vis[p] = x
        
        outs.append('SI' if flg else 'NO')
        
        for x in nums:
            for p in prime_factor(x):
                vis[p] = 0
    
    print('\n'.join(outs))