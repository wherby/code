# 感染传播方法，也是DSU的变种， 感染的时候只能直接接触，传播扩散的时候用DFS，这样也可以获得DSU同样结果
# state[x][y] == 1 and dfs(x, y) 这样是传播关键算法，如过隔壁没有被感染，且可以被感染，则传播有效，DFS

from typing import List, Tuple, Optional
class Solution:
    def latestDayToCross(self, m: int, n: int, cells: List[List[int]]) -> int:
        DIRS = (0, -1), (0, 1), (-1, 0), (1, 0)  # 左右上下

        # 0：水
        # 1：陆地（未被感染）
        # 2：陆地（已被感染）
        state = [[0] * n for _ in range(m)]

        # 能否从第一行到达 (r, c)
        def can_reach_from_top(r: int, c: int) -> bool:
            if r == 0:  # 已经是第一行
                return True
            for dx, dy in DIRS:
                x, y = r + dx, c + dy
                if 0 <= x < m and 0 <= y < n and state[x][y] == 2:
                    return True
            return False

        # 从 (r, c) 出发，能否到达最后一行
        def dfs(r: int, c: int) -> bool:
            if r == m - 1:
                return True
            state[r][c] = 2  # 感染
            for dx, dy in DIRS:
                x, y = r + dx, c + dy
                # 传播病毒到未被感染的陆地
                if 0 <= x < m and 0 <= y < n and state[x][y] == 1 and dfs(x, y):
                    return True
            return False

        for day in range(len(cells) - 1, -1, -1):
            r, c = cells[day]
            r -= 1  # 改成从 0 开始的下标
            c -= 1
            state[r][c] = 1  # 未被感染的陆地
            if can_reach_from_top(r, c) and dfs(r, c):
                return day

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/last-day-where-you-can-still-cross/solutions/936629/dao-xu-bing-cha-ji-by-endlesscheng-canj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。