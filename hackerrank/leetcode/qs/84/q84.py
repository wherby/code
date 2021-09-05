#Largest Rectangle in Histogram
#https://leetcode.com/problems/largest-rectangle-in-histogram/description/



class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)  # make sure [1,2,3,4,5] will calculate on last element.
        stack = [-1]      # make suer hava element on stack
        ans =0
        n =len(heights)
        for i in range(n):
            while heights[i] <heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] -1
                ans = max(ans, h*w)
            stack.append(i)
        heights.pop()
        return ans



s = Solution()
heights = [1,2,3,4,5]
print s.largestRectangleArea(heights)