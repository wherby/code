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
    def perfectPairs(self, nums: List[int]) -> int:
        zero = 0
        for a in nums:
            if a == 0:
                zero +=1
        cnt =0
        if zero>1:
            cnt += zero *(zero-1)//2
        def getNumber(nums,d):
            num1,num2 =[],[]
            zero =0
            for a in nums:
                if a >0:
                    num1.append(a)
                elif a < 0:
                    num2.append(a)
                else:
                    zero +=1
            num1.sort()
            num2.sort()
            sl=[]
            cnt =0
            for a in num1:
                k = bisect_left(sl,(a+1)//2)
                cnt += len(sl) - k
                k1 = bisect_left(num2,-a*2)
                #print(cnt)
                k2 = bisect_right(nums,-((a+d)//2))
                cnt += max(k2-k1,0)
                sl.append(a)
                print(a,cnt,k2,k1,num2,-((a+d)//2),d)
            return cnt
        cnt += getNumber(nums,1)
        nums2 = [-a for a in nums]
        cnt += getNumber(nums2,1)
        return cnt
        



#re =Solution().perfectPairs([9,-4])

#re =Solution().perfectPairs([-3,2,-1,4])
re =Solution().perfectPairs([-6,-2,6])

print(re)