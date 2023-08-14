from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        l,r =1,n
        ls2 = [(nums2[i],i) for i in range(n)]
        ls2.sort()
        def verify(mid):
            cnt =0
            ret = []
            sm =0
            for i in range(n):
                ret.append((nums1[i] +nums2[i]*mid,i,nums1[i]+nums2[i]*mid))
                sm += nums1[i] + mid*nums2[i]
            ret.sort()
            #print(sm)
            for i in range(mid):
                sm -= ret[-1][2]
                #print(sm,ret[-1][0],ret[-1],ret)
                ret.pop()
                ts =[]
                for _,idx,b in ret:
                    ts.append((nums1[idx] + (mid-1-i)*nums2[idx],idx,nums1[idx] + (mid-i-1)*nums2[idx]))
                ts.sort()
                ret = ts
            #print(sm)
            return sm <=x
        for i in range(0,n+1):
            if verify(i):
                return i 
        #verify(2)
        return -1
        





#re =Solution().minimumTime([1,7,6,2,9],[4,2,3,3,0],23)
re =Solution().minimumTime(nums1 = [1,2,3], nums2 = [1,2,3], x = 4)
print(re)