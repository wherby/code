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
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        @cache 
        def f(i,is_limit,is_num,s,state,last,cnt):
            if i == len(s):
                return cnt
            res = 0
            if not is_num:
                res = f(i+1,False,False,s,-1,-1,cnt)
            up = int(s[i]) if is_limit else 9 
            for d in range(0 if is_num else 1, up +1):
                if state == -1:
                    res += f(i+1,is_limit and d == up, True,s,0,d,cnt)
                else:
                    if d >last:
                        if state ==2:
                            res += f(i+1,is_limit and d == up, True,s,1,d,cnt+1) 
                        else:
                            res += f(i+1,is_limit and d == up, True,s,1,d,cnt)
                    elif d < last:
                        if state ==1:
                            res += f(i+1,is_limit and d == up, True,s,2,d,cnt+1) 
                        else:
                            res += f(i+1,is_limit and d == up, True,s,2,d,cnt)
                    elif d== last:
                        res += f(i+1,is_limit and d == up, True,s,0,d,cnt)
            return res 
        a1 = f(0,True,False,str(num2),-1,-1,0)
        a2 = f(0,True,False,str(num1-1),-1,-1,0)
        #@print(a1,a2)
        return a1-a2
            




re =Solution().totalWaviness(4848,4848)
print(re)