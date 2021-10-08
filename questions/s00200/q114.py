#https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def preOrd(root):
            if root == None :
                return None
            #print(root.val)
            left = preOrd(root.left)
            right = preOrd(root.right)
            root.right = left
            root.left = None
            pnext = root
            while pnext.right != None:
                pnext = pnext.right
            pnext.right = right
            return root
        res= preOrd(root)
        return res