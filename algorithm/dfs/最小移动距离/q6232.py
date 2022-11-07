# 
# https://leetcode.cn/contest/weekly-contest-318/problems/minimum-total-distance-traveled/
# 
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort()
        factory.sort()
        n = len(robot)
        m = len(factory)
        @cache
        def dfs(idx,faidx,cnt):
            if idx == n:return 0 
            if faidx == m : return 10**20
            if cnt == factory[faidx][1]: return dfs(idx,faidx+1,0)
            if faidx == m : return 10**20
            ret = abs(robot[idx] - factory[faidx][0]) + dfs(idx+1,faidx,cnt +1)
            ret = min(ret,dfs(idx, faidx+1,0))
            return ret
        return dfs(0,0,0)
