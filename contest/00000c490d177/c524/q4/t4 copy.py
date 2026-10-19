# https://leetcode.cn/contest/weekly-contest-524/problems/minimum-interval-selection-to-cover-target-intervals/description/
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
    def minSelection(self, availableIntervals: List[List[int]], targetIntervals: List[List[int]]) -> int:

        if not targetIntervals:
            return 0
        coords = set()
        for s, e in availableIntervals:
            coords.add(s)
            coords.add(e)
        for s, e in targetIntervals:
            coords.add(s)
            coords.add(e)
            
        sorted_coords = sorted(list(coords))
        coord_to_idx = {val: idx for idx, val in enumerate(sorted_coords)}
        m = len(sorted_coords)
        

        farthest = [-1] * m
        for s, e in availableIntervals:
            u = coord_to_idx[s]
            v = coord_to_idx[e]
            farthest[u] = max(farthest[u], v)
            
        for i in range(1, m):
            farthest[i] = max(farthest[i], farthest[i - 1])
            
        targetIntervals.sort(key=lambda x: x[0])
        merged_targets = []
        for interval in targetIntervals:
            if not merged_targets or merged_targets[-1][1] < interval[0]:
                merged_targets.append(list(interval))
            else:
                merged_targets[-1][1] = max(merged_targets[-1][1], interval[1])
                
        count = 0
        curr = -1  
        
        for t_start, t_end in merged_targets:
            t_s_idx = coord_to_idx[t_start]
            t_e_idx = coord_to_idx[t_end]
            
            if curr < t_s_idx:
                next_reach = farthest[t_s_idx]
                if next_reach <= curr:
                    return -1
                curr = next_reach
                count += 1
            while curr < t_e_idx:
                next_reach = farthest[curr]
                if next_reach <= curr:
                    return -1
                curr = next_reach
                count += 1
        return count

# 测试用例验证：
sol = Solution()
print(sol.minSelection([[1,2],[3,4]], [[1,4]])) # 输出: -1
print(sol.minSelection([[3,29],[2,2],[30,30]], [[3,9],[2,2],[28,28],[7,7],[20,25],[5,28],[29,29],[16,16],[10,10],[16,29],[23,23],[20,20],[12,12],[11,11],[26,26],[30,30],[3,3],[13,13],[21,21]])) # 输出: 3



re =Solution().minSelection([[3,29],[2,2],[30,30]],
[[3,9],[2,2],[28,28],[7,7],[20,25],[5,28],[29,29],[16,16],[10,10],[16,29],[23,23],[20,20],[12,12],[11,11],[26,26],[30,30],[3,3],[13,13],[21,21]])
print(re)
 #availableIntervals = [[1,2],[3,4]], targetIntervals = [[1,4]]