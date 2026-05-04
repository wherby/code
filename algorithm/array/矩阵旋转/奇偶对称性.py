# https://leetcode.cn/problems/rotate-image/description/?envType=daily-question&envId=2026-05-04
# 使用i,j不同的取值，可以包含矩阵奇偶情况的旋转空间
from typing import List, Tuple, Optional
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range((n+1)//2):
            for j in range((n)//2):
                matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i],matrix[i][j]=matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i]