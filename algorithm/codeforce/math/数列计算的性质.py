# https://codeforces.com/gym/104523/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0224/solution/cf104523a.md
# Cascading Sums - 数列计算的性质，对于每个数字，对应的计算结果是一定递增且不会重复的
# 所以原题变化为找到n为数列计算上界的最大原数字


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    def check(x):
        ans = 0
        while x:
            ans += x
            x //= 10
        return ans
    
    for _ in range(t):
        n = II()
        l, r = 1, 10 ** 18
        
        while l <= r:
            mid = (l + r) // 2
            
            if check(mid) > n: r = mid - 1
            else: l = mid + 1
        
        outs.append(n - r)
    
    print('\n'.join(map(str, outs)))