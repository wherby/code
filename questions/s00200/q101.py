# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isS(left, right):
            if left == None or right == None:
                return left ==right
            return left.val == right.val and isS(left.left,right.right) and isS(left.right,right.left)
        if root  == None:
            return True
        return isS(root.left,root.right) 
            
