
from functools import cache

MOD = 1_000_000_007

# (i, j)：当前位置 
# pre_row：上一行（i+1 行）的颜色
# cur_row：当前这一行已填入的颜色
@cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
def dfs(i: int, j: int, pre_row: int, cur_row: int) -> int:
    if i == 0:  # 所有格子都已涂色
        return 1  # 找到一个合法方案

    if j == 3:  # i 行已涂色
        # 开始对 i-1 行涂色，cur_row 变成 pre_row
        return dfs(i - 1, 0, cur_row, 0)

    res = 0
    for color in range(3):  # 枚举 (i, j) 的颜色 color
        # 不能和下面相邻格子 (i+1, j) 颜色相同
        # 不能和左侧相邻格子 (i, j-1) 颜色相同
        if pre_row and color == pre_row >> (j * 2) & 3 or \
                 j and color == cur_row >> ((j - 1) * 2) & 3:
            continue
        res += dfs(i, j + 1, pre_row, cur_row | (color << (j * 2)))
    return res % MOD

class Solution:
    def numOfWays(self, n: int) -> int:
        return dfs(n, 0, 0, 0)  # 从最后一行开始涂色

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/number-of-ways-to-paint-n-3-grid/solutions/3869310/san-chong-fang-fa-ji-yi-hua-sou-suo-di-t-tell/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。