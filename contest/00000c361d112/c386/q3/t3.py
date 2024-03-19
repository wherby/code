from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf
from collections import Counter
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        sm = sum(nums)
        n = len(changeIndices)  
        m = len(nums)
        c = Counter(changeIndices)
        if sm+m>n or len(c.items())!=m:
            return -1
        l,r = sm+m,n
        #\print(l,r)
        #print(len(c),c)
        
        def verify(mid):
            ls = changeIndices[:mid]
            dic = {}
            #print(ls)
            for i,a in enumerate(ls):
                dic[a] = i+1
            if len(dic) != m:
                return False
            kls = [(v,k) for k,v in dic.items()]
            kls.sort()
            used = 0
            for i,(v,k) in enumerate(kls):
                used += nums[k-1]
                #print("a",mid,used,v,k,used + i+1)
                if used + i+1 >v:
                    return False
            return True
                
        
        while l<r:
            mid = (l+r)>>1
            if not verify(mid):
                l = mid+1
            else:
                r=mid
        return l
                
        
            





re =Solution().earliestSecondToMarkIndices([0],[1,1,1])
print(re)