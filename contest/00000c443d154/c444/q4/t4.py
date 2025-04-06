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
    def minimumPairRemoval(self, nums: List[int]) -> int:
        sl=SortedList([])
        mn = nums[0]
        n = len(nums)
        if len(nums) <=1:
            return 0
        if len(nums) ==2 and nums[0] > nums[1]:
            return 1
        for i in range(1,n):
            sl.add((nums[i-1] + nums[i], i))
        pre =[i-1 for i in range(n)]
        dic ={}
        cnt =0
        while sl[0][1] != 1:
            #print(sl)
            a,b =sl[0]
            sl.remove((a,b))
            if pre[b] in dic:
                continue
            nums[b]=nums[pre[b]] + nums[b]
            dic[pre[b]] =1
            while pre[pre[b]] in dic:
                pre[b] = pre[pre[b]]
            pre[b] = pre[pre[b]]
            cnt +=1
            sl.add((nums[b] + nums[pre[b]],b))
            print(sl,pre)
        return cnt


re =Solution().minimumPairRemoval([2,2,-1,3,-2,2,1,1,1,0,-1])
print(re)