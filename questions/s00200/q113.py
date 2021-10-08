#https://leetcode-cn.com/problems/path-sum-ii/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        isFind =[]
        def dfs(root,num,arr):
            if root == None :
                return 
            if root.left ==None and root.right == None and root.val + num == targetSum:
                isFind.append(arr + [root.val])
            dfs(root.left, num + root.val,arr +[root.val])
            dfs(root.right, num + root.val,arr + [root.val])
        dfs(root,0,[])
        return isFind