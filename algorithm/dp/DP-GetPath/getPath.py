# https://leetcode.cn/problems/find-the-minimum-cost-array-permutation/description/
## Get Path
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
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)

        @cache
        def calc(state,pre):
            if state== (1<<n) -1:
                return abs(pre-nums[0])
            res = 10**10
            for i in range(n):
                if (1<<i)&state == 0:
                    res = min(res,calc(state| 1<<i,i) + abs(pre-nums[i]))
            return res
        calc(1,0)
        ## 获取最佳路径
        ret = []
        def getPath(state,pre):
            ret.append(pre)
            if state== (1<<n) -1:
                return 
            finalAns = calc(state,pre)  ##获取最佳答案
            for i in range(n):
                if (1<<i)&state == 0:
                    if calc(state| 1<<i,i) + abs(pre-nums[i]) == finalAns:   ## 比较选择路径是否最佳答案
                        getPath(state | 1<<i,i) 
                        break
        getPath(1,0)
        return ret
# nums[0] = perm[nums[-1]]

re =Solution().findPermutation(  [0,2,1])
print(re)