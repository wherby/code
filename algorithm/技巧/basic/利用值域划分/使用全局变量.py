from typing import List, Tuple, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isG = True
        def dfs(node):
            nonlocal isG 
            if node ==None:
                return 0 
            lh= dfs(node.left)
            rh = dfs(node.right)
            if abs(lh-rh)>1:
                isG = False
            return max(lh,rh)+1
        dfs(root)
        return isG