# https://codeforces.com/gym/105427/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0124/solution/cf105427a.md
# 带入数字计算
# 会有类似进制的表现，把每个进制的长度和对应的1 的数量计算出来


import init_setting
from cflibs import *
def main(): 
    n, k = MII()
    vals = [k + 1]
    cnt = [1]
    
    while vals[-1] < n and len(vals) < k:
        vals.append(vals[-1] * k + 1)
        cnt.append(cnt[-1] * k + 1)
    
    ans = fmax(n - vals[-1], 0)
    n -= ans
    
    for i in range(len(vals) - 1, -1, -1):
        x, n = divmod(n, vals[i])
        ans += x * cnt[i]
    
    print(ans)