# https://leetcode.cn/problems/minimum-cost-to-convert-string-ii/description/?envType=daily-question&envId=2026-01-30
# 题目里描述了两种操作，其实第一种操作是无意义的，因为更换字符只与成本，源目标的字符有关，与是否在同一个字符串无关，因为只有被替换的字符才会影响成本

from typing import List, Tuple, Optional
from collections import defaultdict,deque
from math import inf
from functools import cache

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        len_to_strs = defaultdict(set)
        dis = defaultdict(lambda: defaultdict(lambda: inf))
        for x, y, c in zip(original, changed, cost):
            len_to_strs[len(x)].add(x)  # 按照长度分组
            len_to_strs[len(y)].add(y)
            dis[x][y] = min(dis[x][y], c)
            dis[x][x] = 0
            dis[y][y] = 0

        # 不同长度的字符串必然在不同的连通块中，分别计算 Floyd
        for strs in len_to_strs.values():
            for k in strs:
                for i in strs:
                    if dis[i][k] == inf:  # 加上这句话，巨大优化！
                        continue
                    for j in strs:
                        dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

        # 返回把 source[:i] 变成 target[:i] 的最小成本
        @cache
        def dfs(i: int) -> int:
            if i == 0:
                return 0
            res = inf
            if source[i - 1] == target[i - 1]:
                res = dfs(i - 1)  # 不修改 source[i]
            for size, strs in len_to_strs.items():  # 枚举子串长度
                if i < size:
                    continue
                s = source[i - size: i]
                t = target[i - size: i]
                if s in strs and t in strs:  # 可以替换
                    res = min(res, dis[s][t] + dfs(i - size))
            return res
        ans = dfs(len(source))
        return ans if ans < inf else -1

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-cost-to-convert-string-ii/solutions/2577877/zi-dian-shu-floyddp-by-endlesscheng-oi2r/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。