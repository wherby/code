from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        dic =defaultdict(list)
        for i,a in enumerate(nums):
            dic[a].append(i)
        mx = 0
        for k1 in dic.keys():
            ls = dic[k1]
            m = len(ls)
            r = 0
            #print(ls)
            for l,a in enumerate(ls):
                while r <m and ls[r]-a <=r-l +k:
                    
                    mx = max(mx,r-l+1)
                    #print(r,l,ls,ls[r]-a <=r-l +k,ls[r]-a,mx,r-l +k)
                    r +=1
        return mx
            




re =Solution().longestEqualSubarray(nums = [1,1,2,2,1,1], k = 2)
print(re)