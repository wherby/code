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
    def minArraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(lambda:10**30)
        dic[0] = 0  
        acc = t=0
        for a in nums:
            acc =(dic[t]+a)
            t = acc%k
            dic[t] = min(acc,dic[t])
            #print(dic,t,acc)
        return dic[t]




#re =Solution().minArraySum(nums = [71,91,43,49,80,93,65], k = 205)
re = Solution().minArraySum([58,68,57,71,52,6,40,22,13,29,26,17,47,31,51,73,59,69,37,14],34)
#re = Solution().minArraySum( nums = [3,1,4,1,5], k = 3)
print(re)