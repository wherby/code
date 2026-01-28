# https://codeforces.com/gym/105125/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0126/solution/cf105125c.md
# 贪心寻找当前列的最小值。同时利用前缀和获得当前值在同一列中的个数（就是挑选了当前的相同字符时，前缀也相等的个数），从而更新下一列的可选范围。

import init_setting
from cflibs import *
def main(): 
    n, m = MII()
    cnt = [0] * (n * m + 1)
    for x in MII():
        cnt[x] += 1
    
    vals = []
    for i in range(n * m + 1):
        for j in range(cnt[i]):
            vals.append(i)
    
    for i in range(n * m):
        cnt[i + 1] += cnt[i]
    
    outs = []
    
    for i in range(1, n + 1):
        start = -1
        cur = i
        ans = []
        
        for _ in range(m):
            start += cur
            ans.append(vals[start])
            cur = fmin(cur, start - cnt[vals[start] - 1] + 1)
    
        outs.append(' '.join(map(str, ans)))
    
    print('\n'.join(outs))