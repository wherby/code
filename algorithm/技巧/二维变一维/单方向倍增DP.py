# https://codeforces.com/gym/104017/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0821/solution/cf104017i.md
# 对于题解中 “global flg” 会出错，导致找不到flg 正确更新，需要改成“nonlocal flg”
# 这里使用把无效的dp值设置成inf的方式，把segtree的查找从双变量变成单变量

import init_setting
from lib.cflibs import *
from lib.segmentTreeWithFuction import SegTree
def main():
    t = II()
    outs = []
    
    inf = 10 ** 6
    
    for _ in range(t):
        n, a, b = MII()
        nums = LII()
        
        a -= 1
        b -= 1
        
        dp = [inf] * n
        dp[a] = 0
        
        flg = True
        
        while flg:
            flg = False
            
            def solve():
                nonlocal flg
                
                seg = SegTree(fmin, inf, n)
                updates = [[] for _ in range(n)]
                
                for i in range(n):
                    for x in updates[i]:
                        seg.set(x, inf)
                    
                    v = seg.prod(fmax(0, i - nums[i]), i)
                    if v + 1 < dp[i]:
                        flg = True
                        dp[i] = v + 1
                    
                    seg.set(i, dp[i])
                    
                    if i + nums[i] + 1 < n:
                        updates[i + nums[i] + 1].append(i)
            
            for _ in range(2):
                solve()
                nums.reverse()
                dp.reverse()
        
        outs.append(dp[b])
    
    print('\n'.join(map(str, outs)))

main()