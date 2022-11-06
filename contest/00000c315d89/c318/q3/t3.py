from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
#from sortedcontainers import SortedDict,SortedList


import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        acc = 0
        st = []
        dic = {}
        for i in range(candidates):
            if (costs[i],i) not in dic:
                dic[(costs[i],i)] = 1
                heapq.heappush(st,(costs[i],i))
            if (costs[n-1-i],n-1-i) not in dic:
                dic[(costs[n-1-i],n-1-i)] = -1
                heapq.heappush(st,(costs[n-1-i],n-1-i))
        left =candidates-1
        right =n-candidates
        for _ in range(k):
            #print(acc,st)
            cidx = heapq.heappop(st)
            co ,_ =cidx
            acc +=co
            v = dic[cidx]
            if v >0:
                left +=1
                if left <n and (costs[left],left) not in dic:
                    dic[(costs[left],left)]=1
                    heapq.heappush(st,(costs[left],left))
            else:
                right -=1
                if right >0 and (costs[right],right) not in dic:
                    dic[(costs[right],right)]=-1
                    heapq.heappush(st,(costs[right],right))
        return acc
            









re =Solution().totalCost(costs = [31,25,72,79], k = 3, candidates = 3)
print(re)