from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root, k: int) -> int:
        ls = [root]
        res = []
        while len(ls)>0:
            tm = []
            acc =0
            for a in ls:
                acc += a.val
                if a.left:
                    tm.append(a.left)
                if a.right:
                    tm.append(a.right)
            res.append(acc)
            ls = tm
        if len(res)<k:
            return -1
        res.sort(reverse= True)
        return res[k-1]




re =Solution()
print(re)