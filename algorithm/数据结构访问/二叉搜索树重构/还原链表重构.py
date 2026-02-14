# https://leetcode.cn/problems/balance-a-binary-search-tree/description/?envType=daily-question&envId=2026-02-09
# 二叉搜索树还原数组 贪心重构
from typing import List, Tuple, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def getOrd(node):
            def dfs(n):
                if n == None:
                    return 
                dfs(n.left)
                ls.append(n.val)
                dfs(n.right)
            ls =[]
            dfs(node)
            return ls 
        
        def bs(ls):
            m = len(ls)
            if m==0:
                return None 
            c= m//2
            n= TreeNode(ls[c],bs(ls[:c]),bs(ls[c+1:]))
            return n 
        ls = getOrd(root)
        return bs(ls )
        