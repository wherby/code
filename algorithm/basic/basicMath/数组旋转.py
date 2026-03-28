# https://leetcode.cn/problems/determine-whether-matrix-can-be-obtained-by-rotation/solutions/815309/mei-ju-xuan-zhuan-ci-shu-by-endlesscheng-xue9/?envType=daily-question&envId=2026-03-22
# 旋转拆分成两个步骤，先轴对称旋转，然后行反转

from typing import List, Tuple, Optional
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def rotate(matrix):
            for i in range(n):
                for j in range(i):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            for i,row in enumerate(matrix):
                row.reverse()
        
        for _ in range(4):
            if mat == target:
                return True 
            rotate(mat)
        return False
