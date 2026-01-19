# https://codeforces.com/gym/105364/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0115/solution/cf105364f.md


## 双目标优化DP， 有个目标是主目标，越大越好，另一个目标此目标。在同等主目标的情况下，越多越好
# 因为一定要有一个亏本的块生成，所以在初始状态的时候，必须有亏本块生成，才能进入DP循环
# dp[nmsk]：记录在消耗特定数量金块（由 nmsk 索引）时的当前总盈利（分）。
# resid[nmsk]：记录在当前盈利下，还没凑成组（即不满 100mg）的黄金毫克数。
# if dp[nmsk] < nx or (dp[nmsk] == nx and resid[nmsk] < ny): 盈利优先：钱赚得越多越好。 盈余次之：如果钱一样多，手里剩下的金子（resid）越多越好，因为这让你距离下一个“保底立方体”更近。
# 因为遍历DP的时候会从小到大经过所有状态空间，所以在内层循环的时候，只需要在每个自由度上增加一即可，获得DP转移

import init_setting
from lib.cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        v = II() * 100
        a, b, c = MII()
        p1, p2, p3 = MII()
        
        def f(i, j, k):
            return (i * (p2 + 1) + j) * (p3 + 1) + k
        
        inf  = 10 ** 9
        dp = [-inf] * (p1 + 1) * (p2 + 1) * (p3 + 1)
        resid = [0] * (p1 + 1) * (p2 + 1) * (p3 + 1)
        
        for i in range(p1 + 1):
            for j in range(p2 + 1):
                for k in range(p3 + 1):
                    if (i * a + j * b + k * c) * 5 > v:
                        nx = v - (i * a + j * b + k * c) * 5
                        ny = 0
                        nmsk = f(i, j, k)
                        if dp[nmsk] < nx or (dp[nmsk] == nx and resid[nmsk] < ny):
                            dp[nmsk] = nx
                            resid[nmsk] = ny
                        
                        x = dp[nmsk]
                        y = resid[nmsk]
                        
                        if i < p1:
                            nx, ny = x, y
                            nmsk = f(i + 1, j, k)
                            
                            if ny + a < 100:
                                ny += a
                            else:
                                nx = nx + v - (ny + a) * 5
                                ny = 0
                            
                            if dp[nmsk] < nx or (dp[nmsk] == nx and resid[nmsk] < ny):
                                dp[nmsk] = nx
                                resid[nmsk] = ny
                        
                        if j < p2:
                            nx, ny = x, y
                            nmsk = f(i, j + 1, k)
                            
                            if ny + b < 100:
                                ny += b
                            else:
                                nx = nx + v - (ny + b) * 5
                                ny = 0
                            
                            if dp[nmsk] < nx or (dp[nmsk] == nx and resid[nmsk] < ny):
                                dp[nmsk] = nx
                                resid[nmsk] = ny
                        
                        if k < p3:
                            nx, ny = x, y
                            nmsk = f(i, j, k + 1)
                            
                            if ny + c < 100:
                                ny += c
                            else:
                                nx = nx + v - (ny + c) * 5
                                ny = 0
                            
                            if dp[nmsk] < nx or (dp[nmsk] == nx and resid[nmsk] < ny):
                                dp[nmsk] = nx
                                resid[nmsk] = ny
        
        outs.append(max(dp))
    
    print('\n'.join(map(str, outs)))