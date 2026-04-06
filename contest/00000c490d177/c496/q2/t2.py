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

ls = [i**3 for i in range(1,1003)]
dic =defaultdict(int)
for i,a in enumerate(ls):
    for j,b in enumerate(ls[:i+1]):
        dic[a+b]+=1
ret = []
for k,v in dic.items():
    if v >1:
        ret.append(k)
ret.sort()

class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        return ret[:bisect_right(ret,n)]





re =Solution().findGoodIntegers(4104)
print(re)