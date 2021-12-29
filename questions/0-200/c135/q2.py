# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def vist(node, sm):
            re = sm
            if node.right:
                re=vist(node.right, sm )
            re += node.val
            node.val = re
            if node.left:
                re=vist(node.left,re)
            return re
        vist(root,0)
        return root