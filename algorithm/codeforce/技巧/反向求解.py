# https://codeforces.com/problemset/problem/1945/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0624/solution/cf1945f.md
# 对于从小到大的时候，需要不断删除candidate的情况，反向操作，从大到小获取candidate

import init_setting
from cflibs import *

def main():
    t = II()
    outs = []

    for _ in range(t):
        n = II()
        nums = LII()
        perm = LGMI()
        
        ans, chosen = 0, 0
        pq = []
        
        for i in range(n - 1, -1, -1):
            heappush(pq, nums[perm[i]])
            while len(pq) > i + 1: heappop(pq)
            if len(pq) == i + 1 and pq[0] * len(pq) >= ans:
                ans = pq[0] * len(pq)
                chosen = len(pq)
        
        outs.append(f'{ans} {chosen}')

    print('\n'.join(outs))