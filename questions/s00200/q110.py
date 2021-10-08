#https://leetcode-cn.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        isV =[True]
        def dfs(root,cnt):
            if root == None:
                return cnt
            left = dfs(root.left,cnt +1)
            right =dfs(root.right, cnt +1)
            if abs(left -right) >1:
                #print(left,right)
                isV[0] = False
            return max(left,right)
        dfs(root,0)
        return isV[0]