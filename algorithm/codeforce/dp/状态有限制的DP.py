# https://codeforces.com/gym/106020/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0625/solution/cf106020g.md
# 题目中两两的异或为质数就对组内因子构成做了限制，所以可以直接DP，
# 题目中使用转移和累加分别计算的方式使得逻辑更清晰


import init_setting
from lib.cflibs import *
def main():
    M = 1 << 20
    pr = [1] * M
    
    pr[0] = 0
    pr[1] = 0
    
    for i in range(2, M):
        if pr[i]:
            for j in range(2 * i, M, i):
                pr[j] = 0
    
    inf = 10 ** 18
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        dp = Counter()
        dp[tuple()] = 0
        
        for value in nums:
            ndp = Counter()
            
            for v in dp:
                ndp[v] = fmax(ndp[v], dp[v])
                
                vals = list(v)
                k = len(vals)
                
                for i in range(1 << k):
                    tmp = [vals[j] for j in range(k) if i >> j & 1]
                    tmp.append(value)
                    
                    l = len(tmp)
                    flg = True
                    
                    for x in range(l):
                        for y in range(x):
                            if not pr[tmp[x] ^ tmp[y]]:
                                flg = False
                    
                    if flg:
                        tmp.sort()
                        tmp = tuple(tmp)
                        ndp[tmp] = fmax(ndp[tmp], dp[v])
            
            dp = ndp
            
            for x in dp:
                dp[x] += sum(x)
        
        outs.append(max(dp.values()))
    
    print('\n'.join(map(str, outs)))