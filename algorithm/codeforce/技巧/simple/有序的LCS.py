# https://codeforces.com/gym/106785/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1027/solution/cf106785f.md
# 这里需要知道最长的前序序列的相对位置是一致的
# 直接使用过滤排序的方式

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        p = LII()
        q = LII()
        
        l, r = 0, fmin(n, m)
        
        while l <= r:
            mid = (l + r) // 2
            
            if [x for x in p if x <= mid] == [x for x in q if x <= mid]: l = mid + 1
            else: r = mid - 1
        
        outs.append(n + m - r * 2)
    
    print('\n'.join(map(str, outs)))