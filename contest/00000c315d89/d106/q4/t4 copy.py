from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        dic = defaultdict(list)
        res =[]
        for i in range(m):
            acc =0
            for j in range(n):
                acc = acc*2+ grid[i][j]
            dic[acc].append(i)
            res.append(acc)
        #print(dic)
        if len(dic[0])>0:
            return dic[0]
        
        vals = set(res)
        for i in vals:
            for j in vals:
                if i&j ==0:
                    return sorted([res.index(i),res.index(j)])
        return []
                    
        



re =Solution().goodSubsetofBinaryMatrix(grid = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]])
print(re)