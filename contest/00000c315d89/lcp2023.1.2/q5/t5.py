from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
# https://leetcode.cn/contest/season/2023-spring/problems/ryfUiz/

import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def getNandResult(self, k: int, arr: List[int], operations: List[List[int]]) -> int:
        acc = 0
        cur =0 
        for a in arr:
            cur = cur^a
        for op,x,y in operations:
            if op ==1 and y:
                acc = acc ^(((1<<k)-1 -cur) 

0 0 1
0 1 1 
1 0 1 
1 1 0
1 0 1 0
0 0 1 0
   



k = 3
arr = [1,2]
operations = [[1,2,3],[0,0,3],[1,2,2]]
re =Solution().getNandResult(k,arr,operations)
print(re)