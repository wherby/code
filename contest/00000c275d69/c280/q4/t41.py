# bruteforce
from functools import lru_cache
class Solution(object):
    def maximumANDSum(self, nums, numSlots):
        ans = 0
        @lru_cache(None)
        def search(state,i,value):
            nonlocal ans
            if i >=len(nums):
                ans = max(ans,value)
                return
            for j in range(numSlots):
                c  =(state >>(2*j)) &3
                if c <2:
                    state2  = (state & ~(3<<(2*j))) |((c+1)<<(2*j))
                    search(state2,i+1,value+(nums[i]&(j+1)))
        search(0,0,0)
        return ans

re = Solution().maximumANDSum(nums = [10,10,1,3,6,13,2], numSlots = 8)
print(re)
re = Solution().maximumANDSum(nums = [4,2,2,11,7,12,9,8], numSlots = 4)
print(re)
