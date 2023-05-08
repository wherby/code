from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        ret = []
        acc = 0
        ls = [0]*n
        for idx,a in queries:
            if idx >0 and ls[idx-1] == ls[idx] and ls[idx] !=0:
                acc -=1 
            if idx <n-1 and ls[idx]== ls[idx+1] and ls[idx+1] !=0:
                acc -=1
            ls[idx] = a 
            if idx >0 and ls[idx-1] == ls[idx] and ls[idx] !=0:
                acc +=1 
            if idx <n-1 and ls[idx]== ls[idx+1] and ls[idx+1] !=0:
                acc +=1
            ret.append(acc)
        return ret




re =Solution().colorTheArray(n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]])
print(re)