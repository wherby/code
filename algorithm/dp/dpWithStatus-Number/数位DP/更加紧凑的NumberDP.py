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
    def countFancy(self, l: int, r: int) -> int:
        @cache
        def is_good(n):
            if n < 10: return True
            s = str(n)
            inc = all(s[i] < s[i+1] for i in range(len(s)-1))
            if inc: return True
            dec = all(s[i] > s[i+1] for i in range(len(s)-1))
            return dec
        
        def countNumber(num):
            nstr = str(num)
            n= len(str(num))

            @cache
            def f(i,is_limit,is_num,lastNum,state,sm):
                if i ==n:
                    stateGood = state != 3
                    return 1 if (stateGood or is_good(sm)) and is_num else 0
                res =0 
                up = int(nstr[i]) if is_limit else 9
                for d in range( up +1):
                    nIs_limit = is_limit and d == up
                    nIs_num = is_num or d > 0
                    if not nIs_num:
                        res += f(i+1,nIs_limit,nIs_num,d,0,0)
                    else:
                        nsum = sm + d
                        nstate = 0
                        if not is_num:
                            nstate = 0
                        elif state ==0:
                            if d > lastNum:
                                nstate = 1
                            elif d < lastNum:
                                nstate = 2
                            else:
                                nstate = 3
                        elif state ==1:
                            if d > lastNum:
                                nstate = 1
                            else:
                                nstate = 3
                        elif state ==2:
                            if d < lastNum:
                                nstate = 2
                            else:
                                nstate = 3
                        else:
                            nstate = 3
                        res += f(i+1,nIs_limit,nIs_num,d,nstate,nsum)
                return res
            ret=  f(0,True,False,-1,1,0)
            f.cache_clear()
            return ret
        return countNumber(r) - countNumber(l-1)




re =Solution().countFancy(8,10)
print(re)