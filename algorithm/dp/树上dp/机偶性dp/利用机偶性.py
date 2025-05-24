from typing import List, Tuple, Optional

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sm = sum(nums)
        inc = []
        for a in nums:
            inc.append((a^k) -a)
        inc.sort(reverse =True)
        n = len(nums)
        for i in range(1,n,2):
            t = inc[i] + inc[i-1]
            if t > 0:
                sm +=t 
        #print(sm, inc)
        return sm