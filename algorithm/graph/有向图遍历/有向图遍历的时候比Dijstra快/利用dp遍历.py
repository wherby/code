# https://leetcode.cn/problems/network-recovery-pathways/solutions/3728371/er-fen-da-an-dag-dppythonjavacgo-by-endl-anax/
from typing import List, Tuple, Optional
from functools import cache
from math import inf

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        max_wt = 0
        for x, y, wt in edges:
            if online[x] and online[y]:
                g[x].append((y, wt))
                max_wt = max(max_wt, wt)

        def check(lower: int) -> bool:
            @cache
            def dfs(x: int) -> int:
                if x == n - 1:  # 到达终点
                    return 0
                res = inf
                for y, wt in g[x]:
                    if wt >= lower:
                        res = min(res, dfs(y) + wt)
                return res
            return dfs(0) <= k

        left, right = -1, max_wt + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/network-recovery-pathways/solutions/3728371/er-fen-da-an-dag-dppythonjavacgo-by-endl-anax/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。