# https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree/
from typing import List, Tuple, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        mx = 0
        inf= 10**9
        def dfs(node):
            nonlocal mx
            if node == None:
                return (inf,-inf,0)
            lmn,lmx,lacc = dfs(node.left)
            rmn,rmx,racc = dfs(node.right)
            if lmx <node.val and rmn > node.val:
                mx = max(mx,lacc+racc+node.val)
                #print(node.val,mx)
                return (min(lmn,node.val),max(rmx,node.val),lacc+racc+node.val)
            return (-inf, inf,0)
        dfs(root)
        return mx