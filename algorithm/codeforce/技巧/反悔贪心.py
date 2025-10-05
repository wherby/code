# https://codeforces.com/gym/100488/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0929/solution/cf100488k.md

import init_setting
from cflibs import *
from heapq import heapreplace
def main():
    n = II()
    nums = LII()
    
    having = []
    
    for i in range(n):
        cur = i // 2 + 1
        
        if len(having) < cur:
            heappush(having, nums[i])
        elif having[0] < nums[i]:
            heapreplace(having, nums[i])
    
    v = sum(having)
    print(v, sum(nums) - v)