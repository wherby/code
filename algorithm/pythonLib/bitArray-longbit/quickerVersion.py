
# https://leetcode.com/contest/weekly-contest-467/problems/subsequence-sum-after-capping-elements/description/
# 51ms vs 970 ms
# longbit operation in python 
from typing import List, Tuple, Optional

from heapq import heappop,heappush 


class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        st = []
        for a in nums:
            heappush(st,a)
        bitMask = (1<<(k+1)) -1 
        cur  =1
        rst = n
        ret =[]
        for i in range(1,n+1):
            while st and st[0]<=i:
                b = heappop(st)
                cur = ((cur<<b)&bitMask) | cur 
                rst -=1
            fd= False

            if fd ==False:
                toV = max(k- rst*i,0)
                for j in range(k,toV-1,-i):
                    
                    if j > k:
                        break
                    if (1<<j)&cur:
                        fd= True
                        break
            ret.append(fd)

        return ret