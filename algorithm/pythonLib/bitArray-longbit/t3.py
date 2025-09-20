# https://leetcode.com/contest/weekly-contest-467/problems/subsequence-sum-after-capping-elements/description/
# slow version 970ms
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
                cur = ((cur<<b)&bitMask) | cur |(1<<b)
                rst -=1
            fd= False
            if (1<<k)&cur:
                fd = True
            if fd ==False:
                for j in range(0,k+1):
                    
                    if j > k:
                        break
                    if (1<<j)&cur:
                        # if i==6:
                        #     print(i,j)
                        if (k-j) %i == 0 and (k-j)//i<=rst:
                            fd= True
                            break
            ret.append(fd)
            # if i ==6:
            #     print(i,bin(cur)[2:],)
        return ret
            



# nums = [11,12,2,8,4,19,10,10,14,20,17,10,2,13,20,15,20,9,13,16]
# k=6
nums = [14,8,9,10,13,5,15,15,1,14,3,15,2,2,15]
k =35

re =Solution().subsequenceSumAfterCapping( [2,6,3,6,5,6,2,8] , 29 )
print(re)