from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ret = [-1]*n
        ret[p] =0
        cnt =0 
        sl = SortedList([])
        for i in range(n):
            sl.add(i)
        for b in banned:
            sl.remove(b)
        st = [p]
        while st:
            tmp =set()
            for a in st:
                ret[a]=cnt
                print(a,sl,st)
                sl.remove(a)
                leftIdx = sl.bisect_left(a-k+1)
                rightIdx = sl.bisect_right(a+k-1)
                for i in range(leftIdx,rightIdx):
                    tmp.add(sl[i])
            cnt +=1
            st = tmp
            print(ret)
        return ret
        
        





re =Solution().minReverseOperations(n = 5, p = 0, banned = [], k = 4)
print(re)