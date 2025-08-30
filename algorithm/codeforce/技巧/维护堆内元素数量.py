# https://codeforces.com/problemset/problem/523/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0830/solution/cf523d.md
# 这里需要维护一个大小为k的堆， 技巧是直接初始化一个大小为k的堆，初始值为0， 然后保持堆大小不变


import init_setting
from cflibs import *
def main():
    n, k = MII()
    cur = [0] * k
    
    outs = []
    
    for _ in range(n):
        s, m = MII()
        x = heappop(cur)
        x = fmax(x, s) + m
        
        outs.append(x)
        heappush(cur, x)
    
    print('\n'.join(map(str, outs)))