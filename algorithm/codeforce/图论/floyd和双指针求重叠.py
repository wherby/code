# https://codeforces.com/gym/106208/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0914/solution/cf106280f.md
# 双指针求可能的重叠时间，遍历所有可能的停靠站



import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        
        dis = [[inf] * n for _ in range(n)]
        for i in range(n):
            dis[i][i] = 0
        
        for _ in range(m):
            u, v, w = MII()
            u -= 1
            v -= 1
            dis[u][v] = fmin(dis[u][v], w)
            dis[v][u] = fmin(dis[v][u], w)
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    dis[j][k] = fmin(dis[j][k], dis[j][i] + dis[i][k])
        
        a, b = MII()
        
        alice = [tuple(MII()) for _ in range(a)]
        bob = [tuple(MII()) for _ in range(b)]
        
        ans = 0
        pta, ptb = 0, 0
        
        while pta + 1 < a and ptb + 1 < b:
            l1, r1, s1, t1 = alice[pta][1], alice[pta + 1][0], alice[pta][2], alice[pta + 1][2]
            l2, r2, s2, t2 = bob[ptb][1], bob[ptb + 1][0], bob[ptb][2], bob[ptb + 1][2]
            s1 -= 1
            t1 -= 1
            s2 -= 1
            t2 -= 1
            
            res = 0
            
            for i in range(n):
                l = fmax(l1 + dis[s1][i], l2 + dis[s2][i])
                r = fmin(r1 - dis[i][t1], r2 - dis[i][t2])
                res = fmax(res, r - l)
            
            ans += res
            
            if r1 < r2: pta += 1
            else: ptb += 1
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))