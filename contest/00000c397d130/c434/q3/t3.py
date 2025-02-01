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
    def maxFrequency(self, nums: List[int], k: int) -> int:
        ss =set(nums)

        def find(tt):
            acc = 0
            ls= []
            for i,a in enumerate(nums):
                if a ==tt:
                    acc +=1
                elif a ==k:
                    acc -=1
                ls.append(acc)
            gain = 0 
            st =[0]
            for a in ls:
                while st and a < st[0]:
                    st.pop()
                st.append(a)
                gain = max(gain,a -st[0])
            return gain
        a1  = len(list(filter(lambda x: x== k,nums)))
        ret = a1
        for b in ss:
            if b == k: continue
            ret = max(ret, a1 + find(b))
        return ret
        





re =Solution().maxFrequency([2,8], k = 8)
print(re)