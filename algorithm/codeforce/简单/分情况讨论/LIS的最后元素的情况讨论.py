# https://codeforces.com/gym/106619/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0716/solution/cf106619l.md



import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, k = MII()
        nums = LII()
        
        cur = 0
        tmp = []
        
        res = []
        
        for i in range(n):
            cur += nums[i]
            if len(tmp) == 0 or tmp[-1] < nums[i]:
                tmp.append(nums[i])
            else:
                tmp[bisect.bisect_left(tmp, nums[i])] = nums[i]
            
            v = len(tmp)
            if v > tmp[-1]:
                res.append(cur + k * (v + v + k - 1) // 2)
            else:
                res.append(cur + k * v)
        
        outs.append(' '.join(map(str, res)))
    
    print('\n'.join(outs))