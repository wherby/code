

from typing import List, Tuple, Optional
class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        ans = 0
        for i in range(32,-1,-1):
            newAns = ans | (1<<i)
            costs = []
            for a in nums:
                b  =  newAns & (~a)
                j = b.bit_length()
                msk = (1<<j) -1
                costs.append((newAns & msk) - (a & msk))
            costs.sort()
            if sum(costs[:m])<=k:
                ans = newAns
            #print(ans,costs,i)
        return ans



re =Solution().maximumAND([82,55,96,50,71,83,45,69,32],50,4)
print(re)

