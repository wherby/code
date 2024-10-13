from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:

        res = []

        def dfs(node ):
            nonlocal res 
            if node == None:
                return (0,True)
            if node.left ==None and node.right==None:
                res.append(1)
                return (1,True)
            ll,islG = dfs(node.left)
            lr,isrG = dfs(node.right)
            if islG == True and isrG == True and ll==lr:
                res.append(ll*2+1)
                return (ll*2+1, True)
            return (-1, False)
        dfs(root)
        res.sort()
        return res[-k] if len(res)>=k else -1






re =Solution()
print(re)