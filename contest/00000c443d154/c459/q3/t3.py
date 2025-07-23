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
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        f = [0] * 64
        
        for i in range(1, 63):
            f[i] = f[i.bit_count()] + 1
        def getN(t):
            if t==1 :
                return 0
            else:
                return f[bin(t).count("1")]
        sls = [SortedList() for _ in range(10)]
        for i,a in enumerate(nums):
            sls[getN(a)].add(i)
        ret = []
        

       # print(f)
        for ops in queries:
            if ops[0] == 1:
                op,l,r,k = ops
                lidx = sls[k].bisect_left(l)
                ridx= sls[k].bisect_right(r)
                #print(ridx,lidx,sls[k],k,sls)
                ret.append(ridx-lidx)
            else:
                op,idx,newV = ops
                t = getN(nums[idx])
                sls[t].remove(idx)
                nums[idx]= newV
                t =  getN(nums[idx])
               #print(t,getN(nums[idx]),newV)
                sls[t].add(idx)
        return ret




re =Solution().popcountDepth(nums = [3,5,6], queries = [[1,0,2,2],[2,1,4],[1,1,2,1],[1,0,1,0]])
print(re)