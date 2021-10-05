# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def verify(root,left,right):
            if root == None:
                return True
            isLeft = True
            isRight = True
            v1 = root.val
            if root.left != None:
                isLeft = verify(root.left,left,v1)
            if root.right != None:
                isRight = verify(root.right,v1,right)
            return v1 > left and v1 < right and isLeft and isRight
        return verify(root, -1000000000000000,100000000000000)