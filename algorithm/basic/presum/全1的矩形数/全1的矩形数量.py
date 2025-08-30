# https://leetcode.cn/problems/count-submatrices-with-all-ones/description/?envType=daily-question&envId=2025-08-21
from typing import List, Tuple, Optional
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])
        ldp = [[0]*(n) for _ in range(m)]
        cnt = 0
        for i,row in enumerate(mat):
            for j,a in enumerate(row):
                if a ==0:
                    continue
                else:
                    ldp[i][j] = ldp[i][j-1] +1
                    mx = ldp[i][j]
                    for k in range(i,-1,-1):
                        mx = min(mx, ldp[k][j])
                        cnt+=mx 
        return cnt

re =Solution().numSubmat(mat = [[1,0,1],[1,1,0],[1,1,0]])
print(re)