# https://leetcode.cn/contest/biweekly-contest-159/problems/kth-smallest-path-xor-sum/description/
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from sortedcontainers import SortedDict,SortedList,SortedSet
class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        n = len(par)
        graph = defaultdict(list)
        for node, parent in enumerate(par):
            graph[parent].append(node)

        node_queries = [[] for node in range(n)]
        for q_idx, (node, k) in enumerate(queries):
            node_queries[node].append((k, q_idx))

        # v1: TLE -> took many re-concatentations & sorting
        # res = all sorted paths
        def solve(node, path):
            path ^= vals[node]
            # paths = [path]
            paths = [SortedSet([path])]
            for child in graph[node]:
                paths.append(solve(child, path))

            # paths = sorted(set(paths))
            paths.sort(key = len)
            biggest = paths.pop()
            for smaller in paths:
                biggest.update(smaller)
            for k, q_idx in node_queries[node]:
                if k <= len(biggest):
                    result[q_idx] = biggest[k - 1]
            return biggest

        result = [-1] * len(queries)
        solve(0, 0)
        return result

re =Solution().kthSmallest(par = [-1,0,1], vals = [5,2,7], queries = [[0,1],[1,2],[1,3],[2,1]])
print(re)