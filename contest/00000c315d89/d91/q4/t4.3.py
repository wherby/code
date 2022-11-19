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
        def verify(l,r):
            while l<r:
                mid = (l+r)>>1
                if getCap(mid):
                    r =mid 
                else:
                    l = mid +1
            return l
        l = verify(1,9)
        fd =-1
        if getCap(l):
            fd = l 
        else:
            l  = verify(1,99)
            if getCap(l):
                fd = l 
            else:
                l = verify(1,999)
                if getCap(l):
                    fd = l 
                else:
                    l= verify(1,9999)
                    if getCap(l):
                        fd = l 
                    else:
                        l = verify(1,99999)
                        if getCap(l):
                            fd = l
        if not getCap(fd):
            return []
        l = fd
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
            
        




re =Solution().splitMessage(message = "baaaababab aabaaba", limit =7)
print(re)