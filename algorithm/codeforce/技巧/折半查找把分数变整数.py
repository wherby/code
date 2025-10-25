# https://codeforces.com/gym/105582/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1023/solution/cf105582g.md
# 把调配盐水的比例转换为每个杯子需要多少盐能达到目标比例
# 折半查找


import init_setting
from cflibs import *
def main(): 
    n, a, b = MII()
    nums = []
    
    for _ in range(n):
        m, t = MII()
        m *= b
        t *= b
        nums.append(m - t // b * a)
    
    k = n // 2
    cnt = Counter()
    
    def f(idx, val):
        if idx == k:
            cnt[val] += 1
            return
        f(idx + 1, val + nums[idx])
        f(idx + 1, val)
    
    f(0, 0)
    
    vals = nums[k:]
    k2 = len(vals)
    
    ans = 0
    
    def g(idx, val):
        global ans
        if idx == k2:
            if -val in cnt:
                ans += cnt[-val]
            return 
        g(idx + 1, val + vals[idx])
        g(idx + 1, val)
    
    g(0, 0)
    
    print(ans - 1)