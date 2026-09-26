# https://codeforces.com/gym/104017/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0821/solution/cf104017i.md
# 对于题解中 “global flg” 会出错，导致找不到flg 正确更新，需要改成“nonlocal flg”
# 这里使用把无效的dp值设置成inf的方式，把segtree的查找变成单变量

# 核心性质推导与解读单向 DP 的局限与突破如果只允许从左往右走（$i < j$）
# ，就是标准的单向 DP，无后效性。但允许掉头（来回走）时，可能会出现“先往右走很远，借由一个大功率电台再跳回左边”的情况。掉头步长的指数级增长 ($O(\log n)$ 次折返)
# 正如提示 2 所证明的：假设从 $x$ 往右走到 $y$，再从 $y$ 折返回到 $x$ 左侧的 $z$。设 $x$ 第一步能跳的最大距离为 $V$。如果 $\vert{}x-z\vert{} \le V$，
# 那么 $x$ 根本不需要先往右跳到 $y$，直接一步就能跳到 $z$。因此，要发生“先往右再往左”且有意义的折返，必有 $\vert{}x-z\vert{} > V$。又因为往右到了 $y$，所以 $\vert{}x-y\vert{} \ge V$。
# 此时折返后从 $y$ 跳到 $z$ 的这一步步长为 $\vert{}y-z\vert{} = \vert{}x-y\vert{} + \vert{}x-z\vert{} > 2V$。结论：每一次有效折返，能够覆盖的步长/跨度相比折返前至少翻倍。在长度为 $n$ 的线段上，最多只需折返 $O(\log n)$ 次，路径长度或控制范围就会覆盖整个区间。
# algorithm/codeforce/技巧/docs/来回选择的时候倍增关系的积累.md

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