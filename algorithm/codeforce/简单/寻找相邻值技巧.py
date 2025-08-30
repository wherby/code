# https://codeforces.com/problemset/problem/1941/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0819/solution/cf1941f.md
# 这里寻找相邻值，先二分求target最近的index. 然后用附近左右一位的index，进行验证


import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, m, k = MII()
        nums = LII()
        
        v1 = LII()
        v2 = LII()
        
        v2.sort()
        
        v = 0
        for i in range(1, n):
            v = fmax(v, nums[i] - nums[i - 1])
        
        cnt = 0
        other_v = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] == v:
                cnt += 1
            else:
                other_v = fmax(other_v, nums[i] - nums[i - 1])
        
        if cnt > 1: outs.append(v)
        else:
            for i in range(1, n):
                if nums[i] - nums[i - 1] == v:
                    # 这里 cpp 会爆 int 哦！
                    target = (nums[i] + nums[i - 1]) // 2
                    
                    ans = v
                    
                    for x in v1:
                        p = bisect.bisect_left(v2, target - x)
                        
                        for j in range(p - 1, p + 2):
                            if 0 <= j < k and nums[i - 1] <= v2[j] + x <= nums[i]:
                                ans = fmin(ans, fmax((v2[j] + x) - nums[i - 1], nums[i] - (v2[j] + x)))
                    
                    outs.append(fmax(ans, other_v))
                    break
    
    print('\n'.join(map(str, outs)))