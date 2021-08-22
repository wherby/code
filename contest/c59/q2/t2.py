import math
class Solution:
    def maxMatrixSum(self, matrix) :
        if len(matrix) ==0:
            return 0
        cnt = 0
        sm =0
        minv = 10000000000
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] <0:
                    cnt += 1
                sm += abs(matrix[i][j])
                if abs(matrix[i][j])<minv:
                    minv=abs(matrix[i][j])
        #print(minv)
        if cnt %2 ==0:
            return sm
        else:
            return sm - 2 *minv


matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
a = Solution().maxMatrixSum(matrix)
print(a)