# https://codeforces.com/problemset/problem/343/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0701/solution/cf343c.md
# M * N 在数轴上匹配，从左到右开始，二分查找最大cost， 如果匹配点在左边，则右端点会有两种情况，如果在右边则直接加上最大cost进行匹配
# 【顺序贪心匹配】


import init_setting
from cflibs import *
def main():
    n, m = MII()
    heads = LII()
    reads = LII()

    l, r = 0, 10 ** 12

    while l <= r:
        mid = (l + r) // 2
        
        pt = 0
        
        for h in heads:
            if h <= reads[pt]:
                target = h + mid
            elif h - reads[pt] <= mid:
                target = fmax(h + (mid - (h - reads[pt])) // 2, h + mid - 2 * (h - reads[pt]))
            else:
                continue
            
            while pt < m and reads[pt] <= target:
                pt += 1
            
            if pt == m:
                break
        
        if pt < m: l = mid + 1
        else: r = mid - 1

    print(l)