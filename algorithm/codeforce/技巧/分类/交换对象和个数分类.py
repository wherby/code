# https://codeforces.com/gym/105712/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/tree/main/daily_problems/2025/02
# 对于只有2个类型的时候，做直接模拟，对于单独3个的情况特判


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        ma = max(nums)
        if ma < 2: outs.append(0)
        elif n == 2:
            x, y = nums
            ans = 0
            while x > 1 or y > 1:
                nx = x // 2
                ny = y // 2
                x %= 2
                y %= 2
                ans += nx + ny
                x += ny
                y += nx
            outs.append(ans)
        elif ma == 3 and sum(nums) == 3:
            outs.append(1)
        else: outs.append(sum(nums) - 1)
    
    print('\n'.join(map(str, outs)))