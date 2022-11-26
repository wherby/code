from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from bisect import bisect_right,insort_left,bisect_left
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root, queries: List[int]) -> List[List[int]]:
        ls = [] 
        def dfs(node):
            if node ==None:
                return
            dfs(node.left)
            ls.append(node.val)
            dfs(node.right)
        dfs(root)
        ret =[]
        for a in queries:
            k = bisect_left(ls,a)
            if k<len(ls) and ls[k] == a :
                ret.append([a,a])
            else:
                if k ==0:
                    ret.append([-1,ls[0]])
                elif k == len(ls):
                    ret.append([ls[-1],-1])
                else:
                    ret.append([ls[k-1],ls[k]])
        return ret





re =Solution()
print(re)