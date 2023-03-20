from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def findScore(self, nums: List[int]) -> int:
        dic ={}
        st =[]
        for i,a in enumerate(nums):
            heapq.heappush(st,(a,i))
        cnt =0
        while st:
            a,i = heapq.heappop(st)
            if i not in dic:
                dic[i]=1
                dic[i+1]=1
                dic[i-1]=1
                cnt +=a 
        return cnt




re =Solution().findScore([2,1,3,4,5,2])
print(re)