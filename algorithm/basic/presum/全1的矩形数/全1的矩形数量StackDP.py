# https://leetcode.cn/problems/count-submatrices-with-all-ones/solutions/3704971/omn-dan-diao-zhan-pythonjavacgo-by-endle-jf8l/?envType=daily-question&envId=2025-08-21
from typing import List, Tuple, Optional

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat[0])
        dp = [0]*n
        ans = 0 
        for row in mat:
            for j,a in enumerate(row):
                if a ==0:
                    dp[j] = 0 
                else:
                    dp[j] +=1
            st = [(-1,0,-1)]
            for j,h in enumerate(dp):
                while st[-1][2] >= h:
                    st.pop()
                left,f,_ = st[-1]
                f += (j-left)*h 
                ans += f 
                st.append((j,f,h))
        return ans

re =Solution().numSubmat(mat = [[1,0,1],[1,1,0],[1,1,0]])
print(re)