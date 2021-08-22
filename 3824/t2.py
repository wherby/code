#https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3824/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
## binary tree 优先剪枝算法
class Solution(object):
    def dfs(self,root):
        if not root.left and not root.right:
            if root.val != 1:
                return True
            else:
                return False
        
        if root.left and self.dfs(root.left):
            root.left = None
        if root.right and self.dfs(root.right):
            root.right =None
        if root.left or root.right or root.val ==1:
            return False
        return True
    def pruneTree(self, root):
        res = self.dfs(root)
        if res == True:
            return None
        else:
            return root