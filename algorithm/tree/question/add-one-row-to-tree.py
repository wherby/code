#https://leetcode.cn/problems/add-one-row-to-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if root == None :
            return
        if depth ==1:
            return TreeNode(val,root,None)
        if depth ==2:
            root.left= TreeNode(val,root.left,None)
            root.right = TreeNode(val,None,root.right)
        else:
            root.left = self.addOneRow(root.left,val, depth -1)
            root.right = self.addOneRow(root.right,val,depth -1)
        return root