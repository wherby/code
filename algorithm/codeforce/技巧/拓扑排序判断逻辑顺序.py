# https://codeforces.com/problemset/problem/1931/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0717/solution/cf1931f.md
# 拓扑排序的时候，如果没有访问到所有的点，则证明图里有环，就是逻辑矛盾

import init_setting
from cflibs import *

def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, k = MII()
        path = [[] for _ in range(n)]
        indeg = [0] * n
        
        for _ in range(k):
            vals = LGMI()
            
            for i in range(2, n):
                indeg[vals[i]] += 1
                path[vals[i - 1]].append(vals[i])
        
        cnt = 0
        stk = [i for i in range(n) if indeg[i] == 0]
        
        while stk:
            u = stk.pop()
            cnt += 1
            
            for v in path[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    stk.append(v)
        
        outs.append('YES' if cnt == n else 'NO')
    
    print('\n'.join(outs))

main()