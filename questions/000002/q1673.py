from typing import List, Tuple, Optional
from heapq import heappop,heappush 
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ret = []
        st = []
        for i in range(n-k):
            heappush(st,(nums[i],i))
        lstI = -1
        for i in range(k):
            heappush(st,(nums[n-k+i],n-k+i))
            while st[0][1] < lstI:
                heappop(st)
            b,idx = heappop(st)
            lstI = idx 
            ret.append(b)
        return ret

re = Solution().mostCompetitive(nums = [3,5,2,6], k = 2)
print(re)