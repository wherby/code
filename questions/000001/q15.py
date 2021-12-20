class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res =[]
        a =-1
        while a < n-1:
            a +=1
            sm = -nums[a]
            left = a +1
            right = n-1
            while left < right:
                if nums[left] + nums[right]== sm:
                    res.append([nums[a],nums[left],nums[right]])
                    left,right = left +1, right -1
                    while left <right and nums[left] == nums[left-1]: 
                        left +=1
                    while left < right and nums[right] == nums[right +1]:
                        right -=1
                else:
                    if nums[left] + nums[right] < sm:
                        left +=1
                    else:
                        right -=1
            while a +1 < n and nums[a] ==nums[a+1]:
                a +=1
        return res
         
re =Solution().threeSum( nums = [-1,0,1,2,-1,-4])
print(re)