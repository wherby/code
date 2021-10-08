#https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res =[]
        stack = [root]

        while len(stack) >0:
            cand =[]
            temp =[]
            for t in stack:
                if t == None:
                    continue
                temp.append(t.val)
                cand.append(t.left)
                cand.append(t.right)
            stack = cand
            if len(temp)>0:
                res.append(temp)
        return res[::-1]