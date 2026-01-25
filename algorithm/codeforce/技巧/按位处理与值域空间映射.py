# https://codeforces.com/gym/105813/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0120/solution/cf105813d.md
# 按位处理的值域空间管理
# 以第一位为例，值域空间为 00， 01,10,11 
# 所以对于第i 位 而言 值域空间为 1<<(i+1), 其中置位的l,r 对应 [1<<l, 1<<(l+1) -1 ]


import init_setting
from cflibs import *
from lib.fenwicktree import FenwickTreeArray
def main(): 
    n, q = MII()
    nums = LII()
    
    vis = [0] * (1 << 20)
    for x in nums:
        vis[x] = 1
    
    fens = []
    for i in range(21):
        cnt = [0] * (1 << i + 1)
        for j in range(1 << i + 1):
            for k in range(j, 1 << 20, 1 << i + 1):
                cnt[j] += vis[k]
        fens.append(FenwickTreeArray(cnt))
    
    outs = []
    for _ in range(q):
        t, x = MII()
        
        if t == 1:
            dx = 1 if vis[x] == 0 else -1
    
            for i in range(21):
                fens[i].add(x % (1 << i + 1), dx)
            
            vis[x] ^= 1
        else:
            ans = 0
            
            for i in range(21):
                l = ((1 << i) - x) % (1 << i + 1)
                r = l + (1 << i) - 1
                
                if r < (1 << i + 1): ans += fens[i].rsum(l, r) % 2 * (1 << i)
                else: ans += (fens[i].rsum(l, (1 << i + 1) - 1) + fens[i].rsum(0, r - (1 << i + 1))) % 2 * (1 << i)
            
            outs.append(ans)
    
    print('\n'.join(map(str, outs)))

main()