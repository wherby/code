# https://leetcode.cn/problems/smallest-subtree-with-all-the-deepest-nodes/description/?envType=daily-question&envId=2026-01-09

from typing import List, Tuple, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(nd):
            if nd ==None:
                return 0,None 
            left,nodeLeft = dfs(nd.left)
            right,nodeRight = dfs(nd.right)

            if left > right:
                return left +1 ,nodeLeft
            if right>left:
                return right+1,nodeRight 
            return left +1 ,nd 
        return dfs(root)[1]
