from typing import List, Tuple, Optional
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        ols,els = [0],[0]
        for i,a in enumerate(nums):
            if i %2 ==0:
                els.append(els[-1]+a)
                ols.append(ols[-1])
            else:
                els.append(els[-1])
                ols.append(ols[-1]+a)
        cnt= 0 
        for i in range(n):
            if els[i] + ols[-1]-ols[i+1] == ols[i] + els[-1] - els[i+1]:
                cnt +=1
        return cnt



re = Solution().waysToMakeFair([2,1,6,4])
print(re)