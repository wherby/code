# https://codeforces.com/gym/102894/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0910/solution/cf102894f.md
# 用反悔贪心，记录每个状态最佳选择。
# 正向贪心就用SL直接求解

import init_setting
from cflibs import *
def main():
    n, k = MII()
    
    caps = LII()
    nums = LII()
    pays = LII()
    
    caps.sort(reverse=True)
    
    pt = 0
    total = 0
    pq = []
    
    for i in sorted(range(k), key=lambda x: -nums[x]):
        while pt < n and caps[pt] >= nums[i]:
            pt += 1
        
        heappush(pq, pays[i])
        total += pays[i]
        
        if len(pq) > pt:
            total -= heappop(pq)
    
    print(total)