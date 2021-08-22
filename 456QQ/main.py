class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        minLs = [nums[0]]*len(nums)
        for i in range(1, n):
            minLs[i] = min(minLs[i-1], nums[i])
        stack = []
        for i in range(n-1, -1, -1):
            if nums[i] > minLs[i]:
                while stack and stack[-1] <= minLs[i]:
                    stack.pop()
                if stack and minLs[i] < stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])


nums = [3, 1, 4, 2]
s = Solution()
re = s.find132pattern(nums)
print(re)
