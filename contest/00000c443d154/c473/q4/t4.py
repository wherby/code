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
from collections import Counter
class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        dic = defaultdict(int)
        acc = 0 
        dic[0] =1
        for a in nums:
            acc += a 
            d = acc%k
            cnt += dic[d]
            dic[d] +=1
            #print(cnt,d,dic)
        c = Counter(nums)
        #print(cnt,c)
        for k1,v in c.items():
            if v < 2:
                continue
            for i in range(1,v):
                if i*k1 %k == 0:
                    cnt -= v-i
                #print(i,cnt,v)
        return cnt





re =Solution().numGoodSubarrays(nums = [2,2,2,2,2,2], k = 6)
print(re)