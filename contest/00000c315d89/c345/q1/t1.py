from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        ls= [0]*n
        acc =0 
        turn =1
        while True:
            #print(ls,acc)
            if ls[acc]==1:
                ret =[]
                for i in range(n):
                    if ls[i] ==0:
                        ret.append(i+1)
                return ret
            else:
                ls[acc]= 1
                acc += turn*k
                acc =acc%n
                turn +=1





re =Solution()
print(re)