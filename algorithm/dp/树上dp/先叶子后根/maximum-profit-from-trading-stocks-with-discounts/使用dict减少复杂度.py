# https://leetcode.cn/problems/maximum-profit-from-trading-stocks-with-discounts/
# 对DP中有效值只用Dict 记录会降低复杂度
from typing import List, Tuple, Optional,Dict
from collections import defaultdict,deque


fmax = lambda a, b: b if b > a else a

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g = [[] for _ in range(n)]
        for x, y in hierarchy:
            g[x - 1].append(y - 1)

        def dfs(x: int) -> List[Dict[int, int]]:
            sub_f = [defaultdict(int) for _ in range(2)]
            sub_f[0][0] = sub_f[1][0] = 0
            for y in g[x]:
                fy = dfs(y)
                for k, fyk in enumerate(fy):
                    nf = defaultdict(int)
                    for j, pre_res_y in sub_f[k].items():
                        for jy, res_y in fyk.items():
                            sj = j + jy
                            if sj <= budget:
                                nf[sj] = fmax(nf[sj], pre_res_y + res_y)
                    sub_f[k] = nf

            f = [None] * 2
            for k in range(2):
                res = sub_f[0].copy()
                cost = present[x] // (k + 1)
                if cost <= budget:
                    earn = future[x] - cost
                    for j, res_y in sub_f[1].items():
                        sj = j + cost
                        if sj <= budget:
                            res[sj] = fmax(res[sj], res_y + earn)
                f[k] = res
            return f

        return max(dfs(0)[0].values())