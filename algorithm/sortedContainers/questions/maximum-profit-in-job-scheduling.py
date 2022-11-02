# https://leetcode.cn/problems/maximum-profit-in-job-scheduling/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        sl = SortedList()
        sl.add((0,0))
        n = len(startTime)
        ls = []
        for i in range(n):
            ls.append((endTime[i],startTime[i],profit[i]))
        ls.sort()
        mx = 0
        for e,s,p in ls:
            idx = sl.bisect_right((s,10**10))
            t = sl[idx-1][1]
            k1 = p+ t
            idx2 = sl.bisect_right((e,0))

            if sl[idx2-1][1]< k1:
                sl.add((e,k1))
            mx = max(mx,k1)
            #print(sl)
        return mx