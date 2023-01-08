from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution(object):
    def maxPower(self, ss, r, k):
        """
        :type stations: List[int]
        :type r: int
        :type k: int
        :rtype: int
        """
        n = len(ss)
        pls = [0]*n
        ss = [0]*r + ss + [0]*r
        l=0
        acc =0
        for i,a in enumerate(ss):
            acc +=a 
            if i >= r*2:
                pls[i-r*2] = acc 
                acc -= ss[i-r*2]
        l ,rr = min(pls),max(pls) + k +4
        def verify(mid):
            st =[]
            cnt =0
            acc =0
            for i,a in enumerate(pls):
                #print(i,a,mid,"aa",st,acc,r)
                while st and st[0][0] ==i :
                    _,b = heapq.heappop(st)
                    acc -=b
                if a +acc >=mid:
                    continue
                else:
                    cnt += mid - a- acc
                    #print(cnt,mid,a)
                    #if r >0:
                    heapq.heappush(st,(2*r+i+1,mid - a- acc))
                    acc = mid-a 
            #print(cnt)
            return cnt <=k
                    
                    
        while l < rr :
            mid = (l+rr+1)>>1
            #print(mid,verify(mid),pls)
            if verify(mid):
                l= mid 
            else:
                rr = mid -1
        return l




re =Solution().maxPower(ss = [1,2,4,5,0], r = 1, k = 1)
print(re)