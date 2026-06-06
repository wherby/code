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
    def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums2)
        bs = int(math.sqrt(n)) if n >0 else 1 
        bn = (n+bs-1) // bs 
        bc = [defaultdict(int ) for _ in range(bn)]
        bacc = [0]*bn 

        for i,a in enumerate(nums2):
            idx = i // bs
            bc[idx][a] +=1
        def updateIdx(i):
            blk = i //bs
            old = nums2[i]
            new = nums2[i] + val 
            bc[blk][old] -=1
            bc[blk][new] +=1
            nums2[i] = new 

        ret = []
        for q in queries:
            if q[0] == 1:
                _,x,y,val = q 
                start = x//bs
                end = y //bs 

                if start == end:
                    for i in range(x,y+1):
                        updateIdx(i)
                else:
                    for i in range(x,(start+1)*bs):
                        updateIdx(i)
                    for i in range(start+1,end):
                        bacc[i] += val 
                    for i in range(end* bs ,y+1):
                        updateIdx(i)
            else:
                tot = q[1]
                ans = 0 
                for x in nums1:
                    target = tot-x 

                    for i in range(bn):
                        realV = target - bacc[i]
                        ans += bc[i][realV]
                ret.append(ans)
        return ret





re =Solution().numberOfPairs(nums1 = [1,1], nums2 = [2,2,3], queries = [[2,4],[1,0,1,1],[2,4]])
print(re)