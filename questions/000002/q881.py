from typing import List, Tuple, Optional
# common include
from typing import List, Tuple, Optional
from collections import defaultdict,deque
import functools
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sl = SortedList([])
        cnt = 0
        for a in people:
            sl.add(a)
        while sl:
            b = sl.pop()
            k = sl.bisect_left(limit -b )
            #print(k,sl,limit-b)
            if k <= len(sl):
                if k<len(sl) and sl[k]<=limit-b:
                    sl.remove(sl[k])
                elif k >0:
                    sl.remove(sl[k-1])
            cnt +=1
        return cnt
    
re = Solution().numRescueBoats(people = [2,2], limit =6)
print(re)