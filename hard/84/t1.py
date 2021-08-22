class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        st = [-1]
        mx =0
        for i in range(len(heights)):
            while heights[i] < heights[st[-1]]:
                k = st.pop()
                mx = max(mx,height[k]*(i-st[-1]-1))
            st.append(i)
        return mx
        


height =[2,1,5,6,2,3]
print(Solution().largestRectangleArea(height))