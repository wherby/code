
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from math import isqrt
# 预处理平方剩余核
MX = 100_001
core = [0] * MX
for i in range(1, MX):
    if core[i] == 0:
        for j in range(1, isqrt(MX // i) + 1):
            core[i * j * j] = i

class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        cnt = defaultdict(int)
        ans = 0

        def dfs(x: int, fa: int) -> None:
            nonlocal ans
            c = core[nums[x]]
            # 本题 x 的祖先不包括 x 自己
            ans += cnt[c]
            cnt[c] += 1
            for y in g[x]:
                if y != fa:
                    dfs(y, x)
            cnt[c] -= 1  # 恢复现场

        dfs(0, -1)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/sum-of-perfect-square-ancestors/solutions/3803792/ping-fang-sheng-yu-he-mei-ju-you-wei-hu-bfyxy/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。