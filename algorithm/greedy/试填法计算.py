# https://leetcode.com/contest/weekly-contest-484/problems/maximum-bitwise-and-after-increment-operations/description/
from typing import List, Tuple, Optional
from heapq import heappop,heappush 
class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        ret = [] 
        fd = False 
        for l in range(32,-1,-1):
            st = []
            msk = 1<<l
            tm = list(ret) + [msk]
            for i,a in enumerate(nums):
                cst = 0 
                a1= a
                for t1 in tm:
                    a1 = a1%(t1*2)
                    if a1<t1:
                        cst += t1 - a1%t1
                        a1 = 0
                    else:
                        a1 = a1 %t1
                heappush(st,(cst,i))
            acc = 0 
            cand =[]

            for _ in range(m):
                cost,idx = heappop(st)
                cand.append([cost,idx])
                acc +=cost 
            if acc<=k:
                ret.append(msk)
        
        return sum(ret)






re =Solution().maximumAND([8],10,1)
print(re)