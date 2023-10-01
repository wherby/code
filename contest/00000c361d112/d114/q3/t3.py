from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        n = len(nums)
        for a in nums:
            for i in range(22):
                if (1<<i) &a :
                    dic[i] +=1
        target = 0 
        for i in range(22):
            if dic[i] == n:
                target += (1<<i)
        if target>0:
            return 1
        cnt =0 
        st = 0
        for a in nums:
            if st ==0:
                cnt +=1
                st = a 
            else:
                st = a & st
            #print(a,st,cnt)
        if st !=0:
            cnt -=1
        return cnt
            
        




re =Solution().maxSubarrays(  [1,0,2,0,1,2])
print(re)