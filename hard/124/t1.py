# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxP(self, root):
        if root == None:
            return 0
        leftp = self.maxP(root.left)
        rightP = self.maxP(root.right)
        pathR = max(root.val + leftp , root.val + rightP,root.val)
        self.ans = max(self.ans,pathR, leftp+ rightP + root.val)

        return pathR
        

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = root.val
        self.maxP(root)
        return self.ans
