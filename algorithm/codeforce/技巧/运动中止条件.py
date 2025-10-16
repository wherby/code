# https://codeforces.com/gym/103855/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1014/solution/cf103855e.md
# 运动中止的最终条件排列是可以枚举的

import init_setting
from cflibs import *
def main():
    n, k = MII()
    d = {
        'R': 0,
        'P': 1,
        'S': 2
    }
    
    s = [d[c] for c in I()]
    
    l = 0
    msk = 0
    
    def solve(l, r):
        tmp = [[] for _ in range(3)]
        for i in range(l, r):
            tmp[s[i]].append(i)
        
        if len(tmp[0]) == 0:
            for i in range(l, r):
                s[i] = 2
            
            cur = l - 1
            for i in tmp[1]:
                cur = fmax(cur + 1, i - k)
                s[cur] = 1
        
        elif len(tmp[1]) == 0:
            for i in range(l, r):
                s[i] = 0
            
            cur = l - 1
            for i in tmp[2]:
                cur = fmax(cur + 1, i - k)
                s[cur] = 2
        
        else:
            for i in range(l, r):
                s[i] = 1
            
            cur = l - 1
            for i in tmp[0]:
                cur = fmax(cur + 1, i - k)
                s[cur] = 0
    
    for i in range(n):
        msk |= (1 << s[i])
        if msk == 7:
            solve(l, i)
            l = i
            msk = 1 << s[i]
    
    solve(l, n)
    
    print(''.join('RPS'[i] for i in s))