# https://leetcode.cn/contest/weekly-contest-430/problems/count-special-subsequences/description/
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
from collections import Counter

class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        c1= Counter()
        acc= 0
        for i in range(n-2):
            c2= Counter()
            if i >=4:
                b = nums[i-2]
                for j in range(i-3):
                    c1[nums[j]/b] +=1
                for j in range(i+2,n):
                    c2[nums[j]/nums[i]] +=1
                for k,v in c2.items():
                    acc +=v * c1[k]
        return acc
        





re =Solution().numberOfSubsequences([3,4,3,4,3,4,3,4])
print(re)