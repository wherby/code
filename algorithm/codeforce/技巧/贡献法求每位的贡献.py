# https://codeforces.com/gym/105437/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0525/solution/cf105437h.md
# 使用贡献法，计算每位相同的时候的贡献，这样不用维护左右区域合并查询的问题。

import init_setting
from cflibs import *
def main():
    n = II()
    s = [ord(c) - ord('a') for c in I()]
    
    pref_ch = [0] * (n + 1)
    pref_cnt = [0] * (n + 1)
    
    ch = 0
    cnt = 0
    cur = 0
    
    for i in range(n):
        if s[i] != ch:
            ch = s[i]
            cnt = 0
        
        cur += 2 * cnt + 1
        cnt += 1
        
        pref_ch[i + 1] = ch
        pref_cnt[i + 1] = cnt
    
    suff_ch = [0] * (n + 1)
    suff_cnt = [0] * (n + 1)
    
    ch = 0
    cnt = 0
    
    for i in range(n - 1, -1, -1):
        if s[i] != ch:
            ch = s[i]
            cnt = 0
        
        cnt += 1
        
        suff_ch[i] = ch
        suff_cnt[i] = cnt
    
    ans = 0
    
    for i in range(1, n):
        if s[i] != s[i - 1]:
            val = cur
    
            val -= (pref_cnt[i - 1] if s[i - 1] == pref_ch[i - 1] else 0) * 2
            val -= (suff_cnt[i + 1] if s[i] == suff_ch[i + 1] else 0) * 2
            
            val += (pref_cnt[i - 1] if s[i] == pref_ch[i - 1] else 0) * 2
            val += (suff_cnt[i + 1] if s[i - 1] == suff_ch[i + 1] else 0) * 2
            
            ans = fmax(ans, val)
    
    print(ans)