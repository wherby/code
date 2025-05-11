# use external mem for dfs(x: int, fa: int, cd: int, mul: int) state is too large
from typing import List, Tuple, Optional
class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        memo = {}

        # 这里为了计算方便，把 parity 改成 mul = 1 或者 -1
        def dfs(x: int, fa: int, cd: int, mul: int) -> int:
            t = (x, cd, mul)
            if t in memo:
                return memo[t]

            # 不反转
            res = nums[x] * mul
            for y in g[x]:
                if y != fa:
                    res += dfs(y, x, cd - 1 if cd else 0, mul)

            # 反转
            if cd == 0:
                mul *= -1
                s = nums[x] * mul
                for y in g[x]:
                    if y != fa:
                        s += dfs(y, x, k - 1, mul)
                if s > res:
                    res = s

            memo[t] = res
            return res

        return dfs(0, -1, 0, 1)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/subtree-inversion-sum/solutions/3673852/shu-xing-dppythonjavacgo-by-endlesscheng-pjwg/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。