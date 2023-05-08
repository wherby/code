# https://leetcode.cn/problems/1ybDKD/
# https://leetcode.cn/problems/1ybDKD/solution/zhuang-ya-dp-bao-sou-xia-yi-ge-zhuang-ta-9dad/

from typing import List, Tuple, Optional
from functools import cache

TRANS = (
    # (当前序列末尾添加 B 之后的状态，当前序列末尾添加 R 之后的状态)
    (1, 2),   # 0: 空
    (3, 6),   # 1: 一个 B
    (5, 4),   # 2: 一个 R
    (3, -1),  # 3: 连续多个 B
    (-1, 4),  # 4: 连续多个 R
    (-1, 6),  # 5: BR 交替，且以 B 结尾
    (5, -1),  # 6: BR 交替，且以 R 结尾
)

class Solution:
    def getSchemeCount(self, n: int, m: int, a: List[str]) -> int:
        if n < m:  # 保证 n >= m
            a = [list(col) for col in zip(*a)]
            n, m = m, n
        @cache
        def DFS(r: int, mask: int) -> int: #列DP/DFS
            if r == n:
                return 1
            # 写一个爆搜，生成出所有的合法状态
            def dfs(c: int, row_mask: int, col_mask: int) -> int:   ## 行DP/DFS
                if c == m:
                    return DFS(r + 1, col_mask)  # 枚举下一行
                def nxt(color: int) -> int:
                    rm = TRANS[row_mask][color]  # 新的 rowMask
                    if rm < 0: return 0  # 非法
                    c3 = c * 3
                    cm = TRANS[(col_mask >> c3) & 7][color]  # 新的 colMask 的第 c 列
                    if cm < 0: return 0 # 非法
                    cm = col_mask & ~(7 << c3) | (cm << c3)  # 修改 colMask 的第 c 列
                    return dfs(c + 1, rm, cm)
                b = a[r][c]
                if b == 'B':
                    return nxt(0)
                if b == 'R':
                    return nxt(1)
                if b == '.':
                    return dfs(c + 1, row_mask, col_mask)
                return dfs(c + 1, row_mask, col_mask) + nxt(0) + nxt(1)
            return dfs(0, 0, mask)
        return DFS(0, 0)

#作者：endlesscheng
#链接：https://leetcode.cn/problems/1ybDKD/solution/zhuang-ya-dp-bao-sou-xia-yi-ge-zhuang-ta-9dad/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。