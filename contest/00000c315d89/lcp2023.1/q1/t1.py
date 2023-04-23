from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def supplyWagon(self, ss: List[int]) -> List[int]:
        n =len(ss)
        m = n - n//2
        for _ in range(m):
            mn = 10**10
            idx = 0
            for i in range(len(ss)-1):
                if ss[i]+ss[i+1] < mn:
                    mn = ss[i]+ss[i+1]
                    idx = i 
            if idx !=0:
                ss = ss[:idx] + [mn] + ss[idx+2:]
            else:
                ss = [mn] + ss[idx+2:]
            #print(ss)
        return ss

re =Solution().supplyWagon(  [1,3,1,5])
print(re)



