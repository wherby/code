# https://codeforces.com/problemset/problem/75/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0801/solution/cf75d.md
# 最大子串和的前后缀合并


import init_setting
from cflibs import *
def main():
    n, m = MII()
    
    pref = []
    suff = []
    res = []
    total = []
    
    for _ in range(n):
        k, *nums = LII()
        
        cur = 0
        p = -10000
        
        for i in range(k):
            cur += nums[i]
            p = fmax(p, cur)
        
        pref.append(p)
        total.append(cur)
        
        cur = 0
        s = -10000
        
        for i in range(k - 1, -1, -1):
            cur += nums[i]
            s = fmax(s, cur)
        
        suff.append(s)
    
        cur = 0
        r = -10000
        
        for i in range(k):
            cur = fmax(cur, 0) + nums[i]
            r = fmax(cur, r)
        
        res.append(r)
    
    idxs = LGMI()
    
    ans = -10000
    
    cur = 0
    for idx in idxs:
        ans = fmax(ans, res[idx])
        ans = fmax(ans, cur + pref[idx])
        cur = fmax(cur + total[idx], suff[idx])
    
    print(ans)