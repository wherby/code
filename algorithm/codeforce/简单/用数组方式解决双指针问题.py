# 
# https://codeforces.com/problemset/problem/652/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0811/solution/cf652c.md
# 用cnt 和 vis数组解决了冲突判断和消除。
# 因为可以知道每次新的循环开始之前一定没有冲突，所以只需要关心当前点的冲突点是否在l右边到当前点的位置(没有被置0)

import init_setting
from lib.cflibs import *
def main():
    n, q = MII()
    nums = LII()
    
    tmp = [[] for _ in range(n + 1)]
    
    for _ in range(q):
        x, y = MII()
        tmp[x].append(y)
        tmp[y].append(x)
    
    vis = [0] * (n + 1)
    
    l = 0
    ans = 0
    
    for r in range(n):
        vis[nums[r]] = 1
        
        cnt = 0
        for x in tmp[nums[r]]:
            cnt += vis[x]
        
        while cnt:
            for x in tmp[nums[l]]:
                if x == nums[r]:
                    cnt -= 1
            vis[nums[l]] = 0
            l += 1
        
        ans += r - l + 1
    
    print(ans)