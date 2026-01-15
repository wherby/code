# https://leetcode.cn/problems/maximal-rectangle/submissions/690504828/?envType=daily-question&envId=2026-01-11
# 单调栈设计技巧， 多一位数字最小值可以作为边界,在最后的时候遍历到边界的时候，能让所有栈内元素出去
# 初始栈内有-1指向最小值，使得栈不为空，判断条件更简单
from typing import List, Tuple, Optional



class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp =[0]*(n+1)
        mx = 0
        for row in matrix:
            ndp =[0]*(n+1) 
            for i,a in enumerate(row):
                if a =="1":
                    ndp[i] = dp[i] +1
                else:
                    ndp[i] = 0 
            dp = ndp
            st = [-1]
            for i in range(n+1):
                while dp[i] < dp[st[-1]]:
                    w = dp[st.pop()]
                    mx = max(mx,w*(i-1-st[-1]) )
                st.append(i)
        return mx