# https://codeforces.com/gym/105582/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1023/solution/cf105582c.md
# 在求最大值套数的时候，也不知道怎么配方
# 把问题从最大值用二分的思路，求解在一套的资源条件下能否拼凑， 变成多重背包问题



import init_setting
from cflibs import *
def main(): 
    n, mi, ma = MII()
    
    ms = []
    cs = []
    
    for _ in range(n):
        m, c = MII()
        ms.append(m)
        cs.append(c)
    
    M = 10 ** 4
    l, r = 1, 10 ** 6
    dp = [0] * (M + 1)
    
    while l <= r:
        mid = (l + r) // 2
        
        for i in range(M + 1):
            dp[i] = 0
        
        dp[0] = 1
        
        for i in range(n):
            m = ms[i]
            c = cs[i] // mid
            
            for j in range(m):
                bound = -1
                for x in range(j, M + 1, m):
                    if dp[x]:
                        bound = fmax(bound, x + c * m)
                    if x <= bound:
                        dp[x] = 1
        
        flg = False
        for i in range(mi, ma + 1):
            if dp[i]:
                flg = True
        
        if flg: l = mid + 1
        else: r = mid - 1
    
    print(r)