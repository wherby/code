# OT https://leetcode.cn/problems/largest-plus-sign/submissions/
from typing import List, Tuple, Optional
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        g = [[1]*n for _ in range(n)]
        for x,y in mines:
            g[x][y] = 0
        pre = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                pre[i][j] = pre[i][j-1]+ pre[i-1][j] + g[i-1][j-1] - pre[i-1][j-1]
        ret = 0 
        for k in range(1,(n+1)//2+1):
            for i in range(n-k*2 +2):
                for j in range(n-k*2 +2):
                    ##  i,j       i,j+k
                    ##  i+k,j                  i+k,j+2K
                    a = pre[i+k][j+k*2-1] + pre[i+k-1][j] - pre[i+k][j] - pre[i+k-1][j+k*2-1]
                    b = pre[i+k*2-1][j+k] +pre[i][j+k-1] - pre[i][j+k] - pre[i+k*2-1][j+k-1]
                    #print(a,b,i+k,j+k*2-1, i+k-1,j,k)
                    if a == (k*2 -1) and b == (k*2 -1):
                        ret = max(ret, k)
        return ret
        

re = Solution().orderOfLargestPlusSign(5,[[0,0],[0,1],[0,4],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[2,3],[2,4],[3,0],[4,0],[4,1],[4,3],[4,4]])
print(re)