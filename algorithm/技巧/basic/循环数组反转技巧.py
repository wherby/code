# 把循环数组的变换 转换为子数组的翻转运算

from typing import List, Tuple, Optional
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def reverse(l: int, r: int) -> None:
            while l < r:
                x1, y1 = divmod(l, n)
                x2, y2 = divmod(r, n)
                grid[x1][y1], grid[x2][y2] = grid[x2][y2], grid[x1][y1]
                l += 1
                r -= 1

        # 189. 轮转数组
        size = m * n
        k %= size  # 轮转 k 次等同于轮转 k % size 次
        reverse(0, size - 1)
        reverse(0, k - 1)
        reverse(k, size - 1)
        return grid

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/shift-2d-grid/solutions/3998884/liang-chong-fang-fa-chuang-jian-xin-shu-v5kdb/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。