# https://codeforces.com/gym/106628/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0727/solution/cf106628d.md
# 这个图是求MST的最大值，在完全图中，MST的边数是K-1, 且完全图不论怎么分布，LSB的最小值一定至少有 K-1个， 这就是这里能用二分求值的数学原因


import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    rnd = random.getrandbits(30)
    
    for _ in range(t):
        n, k = MII()
        nums = LII()
        
        l = 0
        r = 29
        
        while l <= r:
            mid = (l + r) // 2
            
            msk = (1 << mid) - 1
            cnt = Counter()
            
            for x in nums:
                cnt[(x & msk) ^ rnd] += 1
            
            if max(cnt.values()) >= k: l = mid + 1
            else: r = mid - 1
        
        outs.append((k - 1) << r)
        
    print('\n'.join(map(str, outs)))