# https://leetcode.cn/contest/weekly-contest-317/problems/height-of-binary-tree-after-subtree-removal-queries/
# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/solutions/2757990/python-3-explanation-with-pictures-dfs/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
import collections
class Solution:
    def treeQueries(self, R, Q: List[int]) -> List[int]:
        Depth, Height = collections.defaultdict(int), collections.defaultdict(int)

        def dfs(node, depth):
            if not node:
                return -1
            Depth[node.val] = depth
            cur = max(dfs(node.left, depth + 1), dfs(node.right, depth + 1)) + 1
            Height[node.val] = cur
            return cur
        dfs(R, 0)

        cousins = collections.defaultdict(list) # Group nodes according to their depth. Keep the top 2 heights.
        for val, depth in Depth.items():
            cousins[depth].append((-Height[val], val))
            cousins[depth].sort()
            if len(cousins[depth]) > 2:
                cousins[depth].pop()

        ans = []
        for q in Q:
            depth = Depth[q]
            if len(cousins[depth]) == 1:  # No cousin, path length equals depth - 1.
                ans.append(depth - 1)
            elif cousins[depth][0][1] == q:  # The removed node has the largest height, look for the node with 2nd largest height.
                ans.append(-cousins[depth][1][0] + depth)
			else:   # Look for the node with the largest height.
                ans.append(-cousins[depth][0][0] + depth)
        return ans