
# https://leetcode.cn/problems/find-all-people-with-secret
# 如果不用时间序列DFS，则会更麻烦  algorithm/dfs/时间序列的DFS/如果不用时间序列.py
from typing import List, Tuple, Optional
from collections import defaultdict,deque

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        arr = [[] for _ in range(n)]
        for x, y, t in meetings:
            arr[x].append((y, t))
            arr[y].append((x, t))
        cache = dict()
        cache[0] = 0
        cache[firstPerson] = 0
        q = deque([0, firstPerson])
        while q:
            x = q.popleft()
            for y, t in arr[x]:
                if t >= cache[x] and (y not in cache or cache[y] > t):
                    cache[y] = t
                    q.append(y)
        return list(cache.keys())
