
from typing import List, Tuple, Optional
from math import inf
# 手写 min 更快
min = lambda a, b: b if b < a else a

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n = len(grid[0])
        mx = max(map(max, grid))

        suf_min_f = [inf] * (mx + 2)
        for _ in range(k + 1):
            min_f = [inf] * (mx + 1)

            # 64. 最小路径和（空间优化写法）
            f = [inf] * (n + 1)
            f[1] = -grid[0][0]  # 起点的成本不算
            for row in grid:
                for j, x in enumerate(row):
                    f[j + 1] = min(min(f[j], f[j + 1]) + x, suf_min_f[x])
                    min_f[x] = min(min_f[x], f[j + 1])
   
            # 计算 min_f 的后缀最小值
            for i in range(mx, -1, -1):
                suf_min_f[i] = min(suf_min_f[i + 1], min_f[i])

        return f[n]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-cost-path-with-teleportations/solutions/3755166/wang-ge-tu-dp-hou-zhui-zui-xiao-zhi-you-b014t/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。