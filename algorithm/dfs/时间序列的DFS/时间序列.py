# https://leetcode.cn/problems/find-all-people-with-secret
# 如果不用时间序列DFS，则会更麻烦  algorithm/dfs/时间序列的DFS/如果不用时间序列.py
from typing import List, Tuple, Optional


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        g = [[] for _ in range(n)]
        for a, b, w in meetings:
            g[a].append((b, w))
            g[b].append((a, w))
        g[0].append((firstPerson, 0))
        g[firstPerson].append((0, 0))
        vi = [-1] * n
        def dfs(x: int, t: int):
            if vi[x] != -1 and vi[x] <= t:
                return
            vi[x] = t
            for y, w in g[x]:
                if w >= t:
                    dfs(y, w)
        dfs(0, 0)
        ans = []
        for i, t in enumerate(vi):
            if t >= 0:
                ans.append(i)
        return ans
        