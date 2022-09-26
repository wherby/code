# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from math import inf

from functools import lru_cache
class Solution(object):
    def closeLampInTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        @lru_cache(None) 
        def getRes(node,turned_on,father_turned):
            if father_turned:
                status = 1- node.val
            else:
                status = node.val
            ans = inf
            for i in range(8):
                op1,op2,op3 = (i>>2 &1),(i>>1 &1),i&1
                if (status +op1 + op2+ op3) %2 == turned_on:
                    tot_op= op1 + op2 +op3
                    if op2:
                        flag1 = 1 - turned_on
                    else:
                        flag1 = turned_on
                    flag2 = op3
                    if node.left:
                        tot_op += getRes(node.left,flag1,flag2)
                    if node.right:
                        tot_op += getRes(node.right,flag1,flag2)
                    if tot_op < ans:
                        ans = tot_op
            return ans
        return getRes(root,0,0) 




re =Solution()
print(re)