# https://leetcode.cn/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

#https://leetcode.cn/circle/discuss/F06Kf0/
#提示 1
#如果让你把所有从起点到终点的路径上的格子都做个标记，这些标记的「轮廓」会是什么样的？

#如果可以使矩阵不连通，「轮廓」应该有什么特点？

#提示 2
#如果可以使矩阵不连通，那么你翻转的那个格子必然会使「轮廓」也不连通（断开）。

#如何找到「轮廓」？

#
# #从 (1,0)(1,0) 出发，优先向下走，其次向右走，得到下轮廓。

#从 (0,1)(0,1) 出发，优先向右走，其次向下走，得到上轮廓。

#如果两个轮廓有交集（除了终点），那么翻转交集中的任意一个格子，都可以使矩阵不连通。

#代码实现时，可以直接把下轮廓的格子值修改成 00（除了终点），如果从 (0,1)(0,1) 
# 出发无法到达终点，则说明可以使矩阵不连通。

#作者：灵茶山艾府
#链接：https://leetcode.cn/circle/discuss/F06Kf0/view/NEPZVx/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List, Tuple, Optional
class Solution:
    def isPossibleToCutPath(self, g: List[List[int]]) -> bool:
        m, n = len(g), len(g[0])

        # 下轮廓
        def dfs1(x: int, y: int) -> bool:  # 返回能否到达终点
            if x == m - 1 and y == n - 1: return True
            g[x][y] = 0  # 直接修改
            return x < m - 1 and g[x + 1][y] and dfs1(x + 1, y) or \
                   y < n - 1 and g[x][y + 1] and dfs1(x, y + 1)

        # 上轮廓
        def dfs2(x: int, y: int) -> bool:  # 返回能否到达终点
            return x == m - 1 and y == n - 1 or \
                   y < n - 1 and g[x][y + 1] and dfs2(x, y + 1) or \
                   x < m - 1 and g[x + 1][y] and dfs2(x + 1, y)

        # 提前特判一些可以直接得到答案的情况
        return m * n > 2 and (m == 1 or n == 1 or g[1][0] == 0 or g[0][1] == 0 or g[-2][-1] == 0 or g[-1][-2] == 0 or
               not dfs1(1, 0) or not dfs2(0, 1))

