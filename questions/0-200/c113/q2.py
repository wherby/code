# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def equals(r1,r2):
            if not r1 and not r2: return True
            if not r1 and r2:return False
            if r1 and not r2:return False
            if r1.val != r2.val: return False
            return (equals(r1.left,r2.right) and equals(r1.right,r2.left)) or (equals(r1.left,r2.left) and equals(r1.right,r2.right))
        return equals(root1,root2)