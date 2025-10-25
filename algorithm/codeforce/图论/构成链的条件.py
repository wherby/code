# https://codeforces.com/gym/106132/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1024/solution/cf106132c.md
# 节点连城一条链，则最多有两个点的度是奇数
# 如果是奇数的时候，因为有方向，则遍历两个方向一定能构成
# 如果度都是偶数，则一定可以构成环， 则任一点都可以作为起点

import init_setting
from cflibs import *
def main(): 
    n, m, k = MII()
    nums = LII()
    
    vis = set(nums)
    cnt = Counter()
    
    for x in nums:
        cnt[x] ^= 1
        cnt[(k - x * x) % m] ^= 1
    
    if sum(cnt.values()) > 2:
        exit(print('NO'))
    
    for x in cnt:
        if cnt[x]:
            ans = [x]
            for i in range(n - 1):
                ans.append((k - ans[-1] * ans[-1]) % m)
            
            if sorted(ans) == sorted(nums):
                ans.reverse()
                print('YES')
                exit(print(*ans))
    
    ans = [nums[0]]
    for i in range(n - 1):
        ans.append((k - ans[-1] * ans[-1]) % m)
    
    
    if sorted(ans) == sorted(nums):
        ans.reverse()
        print('YES')
        exit(print(*ans))
    
    print('NO')