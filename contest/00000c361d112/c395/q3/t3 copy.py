from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ls = '{:064b}'.format(x) 
        ls = [a for a in ls]
        ls = ls[::-1]
        acc =0
        cand = []
        n = n-1
        for i in range(64):
            if acc >=n:
                break
            if ls[i] == "0":
                acc += 1<<len(cand)
                cand.append((i,len(cand)))
            if acc >=n:
                break
        #print(cand)
        while n>0:
            if (1<<cand[-1][1])-1 >= n and len(cand)>1  :
                cand.pop()
            else:
                ls[cand[-1][0]] = "1"
                n -= 1<<cand[-1][1]
                cand.pop()
            #print(n,cand)
        ls = ls[::-1]
        ls = "".join(ls)
        return int(ls,2)



re =Solution().minEnd(n = 3, x = 4)
#re =Solution().minEnd(n = 2, x = 7)
#re =Solution().minEnd(n = 6, x = 1)#11
#re =Solution().minEnd(n = 12, x = 1)#23
re =Solution().minEnd(6715154,7193485)
print(re)