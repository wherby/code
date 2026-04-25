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

from collections import Counter

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        c = Counter(s)
        if c["0"] == 0 or c["1"] == 0:
            return 0
            
        dic = defaultdict(list)
        dic[0] = [-1]
        
        cur = 0
        ret = 0
        
        for i, char in enumerate(s):
            cur += 1 if char == '1' else -1
            for diff in [0, 2, -2]:
                target = cur - diff
                
                if target in dic:
                    for start_idx in dic[target]:
                        length = i - start_idx
                        if length <= ret:
                            continue
                        
                        if diff == 0:
                            ret = max(ret, length)
                        elif diff == 2:
                            zeros = length - (length + 2) // 2
                            if c["0"] > zeros:
                                ret = max(ret, length)
                        elif diff == -2:
                            ones = (length - 2) // 2
                            if c["1"] > ones:
                                ret = max(ret, length)
            
            if cur not in dic:
                dic[cur] = [i]
            elif len(dic[cur]) < 2:
                dic[cur].append(i)
                
        return ret







re =Solution().longestBalanced("01111100")
re =Solution().longestBalanced("00111110")
print(re)