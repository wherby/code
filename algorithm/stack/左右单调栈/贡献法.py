# 求所以子数组的最大值减去最小值
# arr[stack[-1]] <= arr[i]  这里 < 和 <= 是在求相等情况下左边优先还是右边优先，都是等价的
from typing import List, Tuple, Optional

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        def getMarks(arr):
            l = [-1]*n 
            r = [n]*n 

            stack = []
            for i in range(n):
                while stack and arr[stack[-1]] <= arr[i]:
                    r[stack.pop()]  = i 
                if stack:
                    l[i] = stack[-1]
                stack.append(i)
            return l, r 
        
        def getSum(l,r):
            acc = 0 
            for i in range(n):
                cnt = (i-l[i]) *(r[i] - i )
                acc += cnt*nums[i]
            return acc
        l,r = getMarks(nums)
        print(l,r)
        maxSum = getSum(l,r)
        l,r = getMarks([-a for a in nums])
        minSum = getSum(l,r)
        print(maxSum,minSum)
        return maxSum - minSum

nums= [1,1,3,2,2,3,3,2,4,5,5,6,6,4,4,5,5,3,3]

re = Solution().subArrayRanges(nums)
print(re)

def verify(nums):
    n = len(nums)
    max_sum = 0
    min_sum = 0
    
    for i in range(n):
        for j in range(i,n):
            max_sum += max(nums[i:j+1])
            min_sum += min(nums[i:j+1])
    print(max_sum,min_sum)
    return max_sum -min_sum

print(verify(nums))