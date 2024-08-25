from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        mx = max(nums)
        n = len(str(mx))

        def getAllCombi(a):
            astr = "0"*(n-len(str(a))) + str(a)
            st= set([a])
            for i in range(n):
                for j in range(i):
                    bstr = astr[:j] + astr[i]+ astr[j+1:i] + astr[j] + astr[i+1:]
                    st.add(int(bstr))
            return list(st)
        
        dic = defaultdict(list)
        sm = 0
        for i,a in enumerate(nums):
            als = getAllCombi(a)
            tmp = set([])
            for b in als:
                for c in dic[b]:
                    tmp.add(c)
            sm += len(tmp)
            for b in als:
                dic[b].append(i)
        return sm





re =Solution().countPairs([1023,2310,2130,213])
print(re)