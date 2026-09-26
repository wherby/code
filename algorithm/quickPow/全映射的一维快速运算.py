# https://codeforces.com/contest/485/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0917/solution/cf485e.md
# 全映射的一维表示法
# 使用倍增快速计算


import init_setting
from cflibs import *
def main():
    s = I()
    n = len(s)
    
    q = II()
    outs = []
    
    def prod(x, y):
        return [y[i] for i in x]
    
    for _ in range(q):
        k, d = MII()
        
        p = list(range(n))
        
        tmp = []
        
        for i in range(d):
            for j in range(i, k, d):
                tmp.append(j)
        
        for i in range(k):
            p[tmp[i]] = i
        
        for i in range(n):
            p[i] = (p[i] - 1) % n
        
        res = list(range(n))
        steps = n - k + 1
        
        for i in range(20):
            if steps >> i & 1: res = prod(res, p)
            p = prod(p, p)
        
        ans = [0] * n
        for i in range(n):
            ans[res[i]] = i
        
        idx = ans.index(0)
        ans = ans[idx:] + ans[:idx]
        
        s = ''.join(s[x] for x in ans)
        
        outs.append(s)
    
    print('\n'.join(outs))