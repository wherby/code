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
    def minimumSubstringsInPartition(self, s: str) -> int:
        dic = {}
        n = len(s)
        
        @cache
        def dfs(idx):
            if idx <0:
                return 0
            mx = idx+1
            dic = defaultdict(int)
            cmx =0
            for j in range(idx,-1,-1):
                dic[s[j]] +=1
                cmx =max(cmx,dic[s[j]])
                if (idx-j+1) % len(dic) ==0:
                    #print(idx,j,len(dic),dic,cmx)
                    if idx-j+1 == len(dic)*cmx:
                        mx = min(mx,dfs(j-1)+1)
                        #print(idx,j,cmx,len(dic),dic)
            return mx 
        return dfs(n-1)
        





re =Solution().minimumSubstringsInPartition("c")
print(re)