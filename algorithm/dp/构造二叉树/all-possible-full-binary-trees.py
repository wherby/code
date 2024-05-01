
# https://leetcode.cn/problems/all-possible-full-binary-trees/?envType=daily-question&envId=2024-04-02
from typing import List, Tuple, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp=[[] for _ in range(11)]
        dp[1] = [TreeNode()]
        for i in range(2,11):
            dp[i] = [TreeNode(0, left,right) for j in range(1,i) for left in dp[j] for right in dp[i-j] ]
        return dp[(n+1)//2] if n%2 else []