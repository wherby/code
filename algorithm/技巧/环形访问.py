from typing import List, Tuple, Optional

DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)  # 右下左上

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m0, n0 = len(grid), len(grid[0])

        # 从外到内枚举圈
        for i in range(min(m0, n0) // 2):
            m, n = m0 - i * 2, n0 - i * 2  # 这一圈的行数和列数
            x, y = i, i  # 这一圈的左上角
            a = []
            for dx, dy in DIRS:
                for _ in range(n - 1):
                    a.append(grid[x][y])
                    x += dx
                    y += dy
                m, n = n, m  # 见 54. 螺旋矩阵 我的题解

            shift = k % len(a)
            a = a[shift:] + a[:shift]

            # 注意此时 (x, y) 又回到了左上角
            j = 0
            for dx, dy in DIRS:
                for _ in range(n - 1):
                    grid[x][y] = a[j]
                    j += 1
                    x += dx
                    y += dy
                m, n = n, m

        return grid

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/cyclically-rotating-a-grid/solutions/846884/go-mo-ni-by-endlesscheng-92l9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。