

from typing import List, Tuple, Optional

# https://leetcode.cn/problems/count-routes-to-climb-a-rectangular-grid/solutions/3872180/qian-zhui-he-you-hua-dppythonjavacgo-by-w3ve2/

class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        MOD = 1_000_000_007
        m = len(grid[0])
        sum_fg = [0] * (m + 1)

        for i, row in enumerate(grid):
            # 从 i-1 行移动到 i 行的方案数
            f = [0] * m
            for j, ch in enumerate(row):
                if ch == '#':
                    continue
                if i == 0:  # 第一行（起点）
                    f[j] = 1  # DP 初始值
                else:
                    f[j] = sum_fg[min(j + d, m)] - sum_fg[max(j - d + 1, 0)]

            # f 的前缀和
            sum_f = [0] * (m + 1)
            for j, v in enumerate(f):
                sum_f[j + 1] = (sum_f[j] + v) % MOD

            # 从 i 行移动到 i 行的方案数
            g = [0] * m
            for j, ch in enumerate(row):
                if ch == '#':
                    continue
                # 不能原地不动，减去 f[j]
                g[j] = sum_f[min(j + d + 1, m)] - sum_f[max(j - d, 0)] - f[j]

            # f[j] + g[j] 的前缀和
            for j, (fj, gj) in enumerate(zip(f, g)):
                sum_fg[j + 1] = (sum_fg[j] + fj + gj) % MOD

        return sum_fg[m]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-routes-to-climb-a-rectangular-grid/solutions/3872180/qian-zhui-he-you-hua-dppythonjavacgo-by-w3ve2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。