from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ret = [-1]*n
        visit={}
        dic ={}
        st =[p]
        for a in banned:
            visit[a] =1
        cnt =0
        k-=1
        while st:
            tmp =[]
            for a in st:
                if a in visit:continue
                ret[a] =cnt
                visit[a] =1
                if a -k >=0 and a-k not in visit:
                    tmp.append(a-k)
                
                if a + k < n and a+k not in visit:
                    tmp.append(a+k)
            st = tmp 
            cnt +=1
        return ret
        
        





re =Solution().minReverseOperations(n = 4, p = 2, banned = [], k = 4)
print(re)