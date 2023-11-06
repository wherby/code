#https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3824/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeNodeWith1(self,root):
        if root.left !=None:
            root.left= self.removeNodeWith1(root.left)
        if root.right != None:
            root.right = self.removeNodeWith1(root.right)
        if root.left == None and root.right == None and root.val != 1:
            return None
        return root
        
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res =self.removeNodeWith1(root)
        return res