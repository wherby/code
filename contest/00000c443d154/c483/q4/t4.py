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
    def minMergeCost(self, lists: List[List[int]]) -> int:
        n = len(lists)


        def dfs(state):
            #print(state,lists)
            if bin(state).count("1") ==1 :
                return 0 
            res = 10**20
            for i in range(n):
                for j in range(i):
                    if (1<<i) &state and (1<<j)&state:
                        la,lb = list(lists[i]),list(lists[j])
                        m1 = len(lists[i]) + len(lists[j])
                        mlist = lists[i] + lists[j]
                        mlist.sort()
                        ca,cb = len(la),len(lb)
                        cost = len(lists[i]) + len(lists[j]) + abs(la[(ca-1)//2] - lb[(cb-1)//2]) 
                        #print(cost,i,j,mlist)
                        nstate = state -(1<<i)
                        lists[j]=mlist
                        res = min(res, dfs(nstate)+cost)
                        lists[i] = la 
                        lists[j] = lb 
            return res 
        return dfs((1<<n) -1)

                        

                    


from input import lists
print(len(lists))


re =Solution().minMergeCost(lists = [[1,3,5],[2,4],[6,7,8]])
print(re)