# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root) -> int:
        res =[]
        def dfs(node):
            if node ==None:
                return [0,0]
            left = dfs(node.left)
            right = dfs(node.right)
            acc = [node.val,1]
            acc0 =acc[0] + left[0] + right[0]
            acc1 = acc[1] + right[1] + left[1]
            if node.val == acc0 //acc1:
                res.append(acc0 // acc1)
            return [acc0,acc1]
        dfs(root)
        print(root)
        return len(res)
            