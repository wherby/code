from bisect import bisect_right
class Solution:
    def smallestDistancePair(self, nums, k: int) -> int:
        nums.sort()
        def find(x):
            cnt = 0 
            for i,a in enumerate(nums):
                t = bisect_right(nums,a+x)
                cnt += t -i-1
            return cnt 
        l = 0 
        r = nums[-1] - nums[0] +100
        while l < r :
            mid = (l+r) >>1
           # print(mid,find(mid))
            if find(mid) <k:
                l = mid +1
            else:
                r = mid 
        return l 
    
re =Solution().smallestDistancePair(nums = [1,6,1], k = 3)
print(re)
                
            
        