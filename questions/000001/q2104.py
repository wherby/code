class Solution(object):
    def subArrayRanges(self, nums):
        n = len(nums)
        minLeft,maxLeft = [0] *n , [0]*n
        minStack,maxStack =[],[]
        for i,num in enumerate(nums):
            while minStack and nums[minStack[-1]] > num:
                minStack.pop()
            minLeft[i] = minStack[-1] if minStack else -1
            minStack.append(i)

            while maxStack and nums[maxStack[-1]] <= num:
                maxStack.pop()
            maxLeft[i] = maxStack[-1] if maxStack else -1
            maxStack.append(i)
        
        minRight ,maxRight = [0]*n,[0] *n
        minStack,maxStack =[],[]
        for i in range(n-1,-1,-1):
            num = nums[i]

            while minStack and nums[minStack[-1]] >= num:
                minStack.pop()
            minRight[i] = minStack[-1] if minStack else n
            minStack.append(i)

            while maxStack and nums[maxStack[-1]] < num:
                maxStack.pop()
            maxRight[i] = maxStack[-1] if maxStack else n
            maxStack.append(i)
        sumMax,sumMin = 0,0
        for i,num in enumerate(nums):
            sumMax += (maxRight[i] - i )* (i-maxLeft[i])* num
            sumMin += (minRight[i] -i )*(i-minLeft[i]) *num
        return sumMax - sumMin

re = Solution().subArrayRanges([1,2,3])
print(re)