from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(queries)
        res=[]
        for a,b in queries:
            c = a ^b
            cs = bin(c)[2:]
            ncs = len(cs)
            idx = s.find(cs)
            if idx ==-1:
                res.append([-1,-1])
            else:
                res.append([idx,idx + ncs-1])
        return res




re =Solution().substringXorQueries(s = "101101", queries = [[0,5],[1,2]])
print(re)
ts = "1101101a10"*1000 +"11111"
for i in range(100000):
    a=ts.find('11111')
    b = ts.find("1a101111")
    #print(a)
print("a")