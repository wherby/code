#https://leetcode-cn.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        isFind =[False]
        def dfs(root,num):
            if root == None :
                return 
            if root.left ==None and root.right == None and root.val + num == targetSum:
                isFind[0] =True
            dfs(root.left, num + root.val)
            dfs(root.right, num + root.val)
        dfs(root,0)
        return isFind[0]