# https://codeforces.com/gym/105109/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0306/solution/cf105109c.md
# 因为要求满足条件的区间数，用每个当前元素作为最大值，枚举左右边界
# 使用枚举左维护右的方式计算满足条件的区间数，因为枚举左的时候，并且需要包含当前点，所以当前情况是r-i个有效区间
# 而因为滑动窗口需要当前窗口的和小于2倍当前值，所以平均情况下，每个点被枚举的次数是常数级别的。


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        ans = 0
        
        for i in range(n):
            cur = 0
            l = i
            while l and cur + nums[l - 1] < nums[i]:
                l -= 1
                cur += nums[l]
            
            r = i + 1
            while l <= i:
                while r < n and cur + nums[r] < nums[i]:
                    cur += nums[r]
                    r += 1
                ans += r - i
                cur -= nums[l]
                l += 1
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))