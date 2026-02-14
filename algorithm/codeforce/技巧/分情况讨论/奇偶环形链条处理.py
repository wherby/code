# https://codeforces.com/gym/106225/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0212/solution/cf106225c.md
# 段数分奇偶讨论，如果是偶数，则是重复的串
# 如果是奇数，则每个段前后可以看做一个链条，每一段都可以表示前后部分的关系，然后一个段的后部分一定会是另一个段的前部分


import init_setting
from cflibs import *

def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        
        lsts = []
        for _ in range(n):
            lsts.append(LII())
    
        if n % 2 == 0:
            vis = [0] * (n * m // 2 + 1)
            
            ans = []
            for x in lsts:
                if vis[x[0]]: continue
                vis[x[0]] = 1
                ans.extend(x)
            
            outs.append(' '.join(map(str, ans)))
        
        else:
            next_pos = [0] * (n * m // 2 + 1)
            idxs = [0] * (n * m // 2 + 1)
    
            for i, lst in enumerate(lsts):
                idxs[lst[0]] = i
                next_pos[lst[0]] = lst[m // 2]
            
            ans = []
            
            cur = lsts[0][0]
            for _ in range(n):
                ans.extend(lsts[idxs[cur]][:m // 2])
                cur = next_pos[cur]
            
            outs.append(' '.join(map(str, ans)))
    
    print('\n'.join(map(str, outs)))