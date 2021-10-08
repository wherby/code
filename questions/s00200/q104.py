#https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findDp(root,dp):
            if root == None:
                return dp
            return max(findDp(root.left,dp+1),findDp(root.right,dp+1))
        return findDp(root,0)