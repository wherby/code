from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        dic={}
        level =0
        st =[(root,root.val)]
        idx =0
        cdic={}
        while st:
            tmp = []
            acc =0
            for a,c in st:
                acc += a.val
                childV = 0
                if a.left:
                    childV +=a.left.val
                if a.right:
                    childV +=a.right.val
                if a.left:
                    tmp.append((a.left,childV))
                if a.right:
                    tmp.append((a.right,childV))
                cdic[idx] = c
                idx +=1
            dic[level] = acc 
            level +=1
            st= tmp
        idx =0
        level =0
        st  =[root]
        while st:
            tmp = []
            lev= dic[level]
            for a in st:
                a.val= lev - cdic[idx]
                if a.left:
                    tmp.append(a.left)
                if a.right:
                    tmp.append(a.right)
                idx +=1
            level +=1
            st =tmp 
        return root
                





re =Solution()
print(re)