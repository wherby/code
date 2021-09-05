#Container With Most Water
#Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
#n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

#Note: You may not slant the container and n is at least 2.
# Find maxV of area

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right =n-1
        mx =0
        while left <right:
            vleft = height[left]
            vright = height[right]
            tv = min(vright,vleft) * (right -left)
            if tv > mx:
                mx = tv
            if vleft> vright:
                right = right -1
            else:
                left = left +1
        return mx

        



s = Solution()
height = [1,2,5,6,3,4,10,22,12,1,10,11]
print s.maxArea(height)