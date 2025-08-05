from typing import List, Tuple, Optional

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        acc = 0 
        for a in nums:
            acc |= a 
        sm =acc 
        cnt = 0 
        n = len(nums)
        for state in range(1,(1<<n)):
            acc = 0
            for i in range(n):
                if (state >> i) &1:
                    acc |=nums[i]
            if acc == sm :
                cnt +=1
            #print(state,acc,cnt)
        return cnt

re = Solution().countMaxOrSubsets(nums = [3,2,1,5])
print(re)