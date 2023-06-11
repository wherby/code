from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        mx = sum(nums)
        n = len(nums)
        nums= nums*2
        for i in range(1,n):
            ret= []
            st = []
            for j in range(n+i):
                heapq.heappush(st,(nums[j],j))
                if j >=i:
                    #print(st[-1],st,j-i)
                    while st[0][1] < j-i:
                        #print(st)
                        heapq.heappop(st)
                    ret.append(st[0][0])
                #print(st,i,j,ret)
            #print(i,ret)
            mx = min(mx,i*x + sum(ret))
        nums = nums[::-1]
        #print(nums)
        for i in range(1,n):
            ret= []
            st = []
            for j in range(n+i):
                heapq.heappush(st,(nums[j],j))
                if j >=i:
                    while st[0][1] < j-i:
                        heapq.heappop(st)
                    ret.append(st[0][0])
                    #print(st,j,ret)
            #print(i,ret)
            mx = min(mx,i*x + sum(ret))
        return mx





re =Solution().minCost([31,25,18,59],27)
print(re)