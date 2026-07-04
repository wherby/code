# https://codeforces.com/gym/106607/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0701/solution/cf106607b.md

import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
    
        l = n
        r = -1
        for i in range(n):
            if nums[i] != 1:
                l = fmin(l, i)
                r = fmax(r, i)
        
        if l > r: outs.append(0)
        else:
            flg = True
            for i in range(l, r + 1):
                if nums[i] != nums[l]:
                    flg = False
            
            outs.append(1 if flg else 2)
    
    print('\n'.join(map(str, outs)))