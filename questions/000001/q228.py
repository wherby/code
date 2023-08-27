from typing import List, Tuple, Optional
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        right = -1
        n = len(nums)
        for i in range(n):
            if i >right:
                for j in range(i+1,n):
                    if nums[j] != nums[j-1] +1:
                        break
                    else:
                        right = j
                if right <= i:
                    res.append(str(nums[i]))
                else:
                    res.append(str(nums[i]) +"->" + str(nums[right]))
        return res

re =Solution().summaryRanges([0,1,2,4,5,7])
print(re)