# 求最小路径和的时候，使用空间降维写法
from typing import List, Tuple, Optional
from math import inf
# 手写 min max 更快
fmin = lambda a, b: b if b < a else a
fmax = lambda a, b: b if b > a else a

class Solution:
    # 64. 最小路径和
    def minPathSum(self, grid: List[List[int]]) -> int:
        f = [inf] * (len(grid[0]) + 1)
        f[1] = 0
        for row in grid:
            for j, x in enumerate(row):
                f[j + 1] = fmin(f[j], f[j + 1]) + fmin(x, 1)  # 值大于 0 的单元格花费 1
        return f[-1]

    def maxPathScore(self, grid: List[List[int]], K: int) -> int:
        if self.minPathSum(grid) > K:
            return -1

        m, n = len(grid), len(grid[0])
        K = fmin(K, m + n - 2)  # 至多花费 m+n-2
        f = [[-inf] * (K + 2) for _ in range(n + 1)]
        f[1][1] = 0

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                for k in range(fmin(K, i + j), -1, -1):  # 从 (0,0) 到 (i,j) 至多花费 i+j
                    new_k = k - 1 if x else k
                    f[j + 1][k + 1] = fmax(f[j + 1][new_k + 1], f[j][new_k + 1]) + x

        return max(f[n])

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-path-score-in-a-grid/solutions/3827073/wang-ge-tu-dppythonjavacgo-by-endlessche-myez/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。