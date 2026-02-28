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
    def countSequences(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ls =[2,3,5]
        dic ={}
        for cur in range(1,7):
            j = cur
            tmp = [0]*3
            for i,a in enumerate(ls):
                while j%a==0:
                    tmp[i]+=1
                    j//=a
            dic[cur] = tmp
        tmp =[0]*3
        j =k 
        for i,a in enumerate(ls):
            while j%a==0:
                tmp[i]+=1
                j//=a
        if j!=1:
            return 0
        target = tuple(tmp)
        @cache
        def dfs(i,pre):
            if i==n:
                return pre == target
            acc =dfs(i+1,pre) + dfs(i+1,tuple([pre[j]+dic[nums[i]][j] for j in range(3)])) +dfs(i+1,tuple([pre[j]-dic[nums[i]][j] for j in range(3)]))  
            return acc
        res= dfs(0,tuple([0]*3))
        dfs.cache_clear()   
        return res




re =Solution().countSequences([5,3,5],3)
print(re)