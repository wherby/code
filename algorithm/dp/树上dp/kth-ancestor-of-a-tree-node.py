# https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/?envType=daily-question&envId=2024-04-06
from typing import List, Tuple, Optional
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.dp = [[0]*(n+1) for _ in range(20)]
        for i,a in enumerate(parent):
            self.dp[0][i+1] = a+1
        for i in range(1,20):
            for j in range(n+1):
                self.dp[i][j] = self.dp[i-1][self.dp[i-1][j]]
        
        


    def getKthAncestor(self, node: int, k: int) -> int:
        a = node+1
        for i in range(19,-1,-1):
            if (1<<i) &k:
                a = self.dp[i][a]
        return a -1
    



# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)