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
    def countNumbers(self, l: str, r: str, b: int) -> int:
        mod =10**9+7
        def toN(s,b):
            ret = []
            while s !=0:
                ret.append(s%b)
                s = s //b 
            ret = list(map(str,ret))
            return "".join(ret[::-1])
        lstr = toN(int(l)-1 ,b)
        rstr = toN(int(r),b)
        
        @cache
        def f(i,frm,is_limit,is_num,s):
            if i ==len(s):
                return int(is_num)
            res =0
            if not is_num:
                res = f(i+1,frm,False,False,s) ##计算 0-9，10-99，100-999，1000-9999
            up = int(s[i]) if is_limit else b-1
            for d in range(frm, up +1):
                res += f(i+1,max(d,frm),is_limit and d ==up, True,s)
            return res
        #print(lstr,rstr,f(0,1,True,False,rstr),f(0,1,True,False,lstr))
        return (f(0,1,True,False,rstr) -f(0,1,True,False,lstr))%mod




re =Solution().countNumbers(l = "2", r = "7", b = 2)
#re =Solution().countNumbers( l = "23", r = "28", b = 8)
print(re)