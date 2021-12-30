# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return True
            isLeft, isR=True,True
            isEqual = True
            if root.left:
                isLeft = dfs(root.left)
                isEqual =root.left.val == root.val
                if isEqual == False:
                    return False
            if root.right:
                isR = dfs(root.right)
                isEqual = root.right.val == root.val
                if isEqual == False:
                    return False
            if isLeft and isR and isEqual:
                return True
            else:
                return False
        return dfs(root)