from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node):
            if node.left ==None:
                return bool(node.val)
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val ==2:
                return left or right
            else:
                return left and right
        return dfs(root)





re =Solution()
print(re)