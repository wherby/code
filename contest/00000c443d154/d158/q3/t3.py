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
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f2ls = [0]*n 
        for i,a in enumerate(nums):
            cnt =  0
            while a %2 ==0:
                cnt +=1
                a = a//2
            nums[i] =a 
            f2ls[i] = cnt
        ret = 0
        for i in range(n):
            gcd = nums[i]
            mx2,mx2cnt = f2ls[i],1
            if k:
                ret = max(ret,gcd*(1<<mx2)*2)
            else:
                ret = max(ret,gcd*(1<<mx2))
            for j in range(i+1,n):
                gcd = math.gcd(gcd,nums[j])
                if f2ls[j]<mx2:
                    mx2 = f2ls[j]
                    mx2cnt =1
                elif f2ls[j]==mx2:
                    mx2cnt +=1
                else:
                    pass 
                if mx2cnt<=k:
                    ret = max(ret,gcd*(1<<mx2)*2 *(j-i+1))
                else:
                    ret = max(ret,gcd*(1<<mx2) *(j-i+1))
        return ret





re =Solution().maxGCDScore( nums = [2,4], k = 1)
print(re)