from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        l,r =1,n+3
        def getCap(k):
            nonlocal n
            s = [str(i) for i in range(1,k+1)]
            st1 =  "".join(s)
            cnt = len(st1) + 3*k  + len(str(k))*k  + n 
            return cnt <= limit*k
        while l<r:
            mid = (l+r)>>1
            if getCap(mid):
                r =mid 
            else:
                l = mid +1
        if l > n:
            return []
        # if l == 1:
        #     return [message+"<1/1>"]
        ret = []
        idx = 0
        for i in range(1,l+1):
            res = limit-3 - len(str(l)) - len(str(i))
            tmp = message[idx:idx+res] + "<" + str(i)+ "/" + str(l)+ ">"
            ret.append(tmp)
            idx = idx +res
        return ret
            
        




re =Solution().splitMessage(message = "this is really a very awesome message", limit = 98)
print(re)