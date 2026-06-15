
# https://leetcode.cn/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/solutions/3980318/wqs-er-fen-aliens-dpdan-diao-dui-lie-you-44mk/

from typing import Callable, List, Tuple
from collections import deque
from math import inf
def aliensDp(k: int, getDp: Callable[[int], Tuple[int, int]]) -> int:
    left, right = 0, int(1e18) 
    f1 = getDp(0)
    if 1<=f1[1]<=k:
        return f1[0]
    penalty = 0
    best_cand = (-inf, 0)
    while left <= right:
        mid = (left + right) >> 1
        cand = getDp(mid)
        if cand[1] >= k:
            penalty = mid
            best_cand = cand
            left = mid + 1
            
            
        else:
            right = mid - 1
    return best_cand[0] + penalty * k
class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        pre = [0]
        for x in nums:
            pre.append(pre[-1]+x)
        def getdp(p):
            f = [[-inf,0] for _ in range(n+1)]
            f[0] = [0,0]
            def fg(x, y):
                cx = f[x][0]-pre[x]
                cy = f[y][0]-pre[y]
                if cy > cx:
                    return True
                if cy==cx and f[y][1]<f[x][1]:
                    return True
                return False
            def max2(a, b):
                if a[0]>b[0]:
                    return a
                if b[0]>a[0]:
                    return b
                return a if a[1]>b[1] else b
            q = deque()
            for i in range(1, n+1):
                while q and q[0] < i-r:
                    q.popleft()
                j = i-l
                if j >= 0:
                    while q and fg(q[-1],j):
                        q.pop()
                    q.append(j)
                f[i] = list(f[i-1])
                if q:
                    na = [f[q[0]][0]-pre[q[0]]+pre[i]-p,f[q[0]][1]+1]
                    f[i] = max2(f[i],na)
            if f[n][1]==0:
                mx = -inf
                q = deque()
                for i in range(1, n+1):
                    while q and q[0] < i-r:
                        q.popleft()
                    j = i-l
                    if j >= 0:
                        while q and pre[j]<pre[q[-1]]:
                            q.pop()
                        q.append(j)
                    if q:
                        mx = max(mx,pre[i]-pre[q[0]])
                return [mx-p, 1]
            return f[n]
        return aliensDp(m, getdp)

# 作者：xswl
# 链接：https://leetcode.cn/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/solutions/3980318/wqs-er-fen-aliens-dpdan-diao-dui-lie-you-44mk/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。