class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <2:
            return 0
        left =height[0]
        right =height[-1]
        leftIndex =0
        rightIndex =len(height)-1
        sm = 0
        while leftIndex < rightIndex:
            if left >right:
                rightIndex = rightIndex -1
                if right > height[rightIndex]:
                    sm += right - height[rightIndex]
                else:
                    right = height[rightIndex]
            else:
                leftIndex +=1
                if left > height[leftIndex]:
                    sm += left - height[leftIndex]
                else:
                    left = height[leftIndex]
        return sm


height = [0,1,0,2,1,0,1,3,2,1,2,1]
a = Solution().trap(height)
print(a)