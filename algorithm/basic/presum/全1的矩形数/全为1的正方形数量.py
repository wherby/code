# https://leetcode.cn/problems/count-square-submatrices-with-all-ones/solutions/3751608/tu-jie-dong-tai-gui-hua-jian-ji-xie-fa-p-1kiy/?envType=daily-question&envId=2025-08-20
# 用前缀和的思想，用三个前缀矩阵组成最大的可能的矩阵
from typing import List, Tuple, Optional

class Solution:
    def countSquares(self, mtx: List[List[int]]) -> int:
        m,n = len(mtx),len(mtx[0])
        dp= [[0]*(n+1) for _ in range(m+1)]
        cnt = 0 
        for i,row in enumerate(mtx):
            for j,a in enumerate(row):
                if a == 0:
                    dp[i+1][j+1] = 0 
                else:
                    dp[i+1][j+1]  = min(dp[i][j],dp[i+1][j], dp[i][j+1]) +1
                    cnt += dp[i+1][j+1]
        return cnt

re =Solution().countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])
print(re)