from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        dic =defaultdict(int)
        for a in basket1:
            dic[a]+=1
        for b in basket2:
            dic[b] +=1
        for k,v in dic.items():
            if v %2 ==1:
                return -1
        mn = min(min(basket1),min(basket2))
        bk1,bk2=SortedList([]),SortedList([])
        dic2 = defaultdict(int)
        for a in basket1:
            dic2[a] +=1
        for k,v in dic.items():
            diff = v//2 - dic2[k]
            if diff >0:
                for _ in range(diff):
                    bk1.add(k)
            else:
                for _ in range(-diff):
                    bk2.add(k)
        sm = 0
        #print(bk1,bk2,mn)
        for a in bk1:
            t= bk2[-1]
            sm += min(2*mn,min(a,t))
            bk2.remove(t)
            #print(a,t,sm,mn,2*mn,min(3*2,min(a,t)))
        return sm




re =Solution().minCost(basket1 = [4,2,2,2], basket2 = [1,4,1,2])
re =Solution().minCost([4,4,4,4,3],[5,5,5,5,3])
print(re)