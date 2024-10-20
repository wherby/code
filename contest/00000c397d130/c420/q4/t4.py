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
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        ans = [None]*n 
        g =[[] for  _ in range(n)]
        ind= [0]*n
        for i,a in enumerate(parent):
            if a >=0:
                g[a].append(i)
                ind[a] +=1
        acc = [[0]*26 for _ in range(n)]
        for i in range(n):
            acc[i][ord(s[i]) -ord('a')] +=1
        cand = []
        for i in range(n):
            if ind[i] == 0:
                cand.append(i)
        while cand:
            a = cand.pop()
            pa = parent[a]
            if pa >=0:
                acc[pa] = [(x+y)%2 for x,y in zip(acc[pa],acc[a]) ]
                ind[pa] -=1
            if ind[pa] ==0:
                cand.append(pa)
            if sum(acc[a])<=1:
                ans[a] = True
            else:
                ans[a] = False
        return ans





re =Solution().findAnswer(parent = [-1,3,0,2,9,7,1,2,7,12,0,7,7,12], s = "ikakdbhhgdbceb")
print(re)