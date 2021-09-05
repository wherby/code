#Maximal Rectangle
#Max Area of rectange in Maxtrix of '1'
#https://leetcode.com/problems/maximal-rectangle/description/

#Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

#For example, given the following matrix:

#1 0 1 0 0
#1 0 1 1 1
#1 1 1 1 1
#1 0 0 1 0

#Return 6.



class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n+1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] ==1 else 0
            stack =[-1]
            for i in range(n+1):
                while  height[i]< height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i-1 - stack[-1]
                    ans = max(ans,h * w)
                stack.append(i)
        return ans


s = Solution()
matrix = [[1,0,1,0,0],
[1, 0, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 0, 0, 1, 0]]

print s.maximalRectangle(matrix)