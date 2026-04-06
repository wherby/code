# https://leetcode.cn/problems/maximum-amount-of-money-robot-can-earn/description/?envType=daily-question&envId=2026-04-02
# f[0][1] = [0] * 3 采用坐标平移技巧，为了使得边界0,0能正确赋值，所以把其中一边的转移设置正确边界条件
# 这里不用判断x是否为正负，因为正的时候是在当前平面转移，负的时候在上层平面转移
# 这里只用返回 f[m][n][2] 因为初始值2 的平面也是0， 这个值包容了使用0,1,2次跳转的情况
from typing import List, Tuple, Optional
from math import inf

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        f = [[[-inf] * 3 for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][1] = [0] * 3
        for i, row in enumerate(coins):
            for j, x in enumerate(row):
                f[i + 1][j + 1][0] = max(f[i + 1][j][0], f[i][j + 1][0]) + x
                f[i + 1][j + 1][1] = max(f[i + 1][j][1] + x, f[i][j + 1][1] + x,
                                         f[i + 1][j][0], f[i][j + 1][0])
                f[i + 1][j + 1][2] = max(f[i + 1][j][2] + x, f[i][j + 1][2] + x,
                                         f[i + 1][j][1], f[i][j + 1][1])
        return f[m][n][2]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-amount-of-money-robot-can-earn/solutions/3045103/wang-ge-tu-dp-by-endlesscheng-g96j/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。