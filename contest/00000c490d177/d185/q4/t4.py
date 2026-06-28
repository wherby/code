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
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        def count(num):
            s  = str(num)
            n = len(s)

            @cache
            def f(i,is_limit,is_num,last):
                if i ==len(s):
                    return int(is_num)
                res =0
                if not is_num:
                    res = f(i+1,False,False,-1) ##计算 0-9，10-99，100-999，1000-9999
                up = int(s[i]) if is_limit else 9
                for d in range(0 if is_num else 1, up +1):
                    if last== -1:
                        res += f(i+1,is_limit and d ==up, True,d)
                    elif abs(last -d) <=k:
                        res += f(i+1,is_limit and d ==up, True,d)
                return res
            return f(0,True,False,-1)
        return count(r) -count(l-1)





re =Solution().goodIntegers(10,15,1)
print(re)