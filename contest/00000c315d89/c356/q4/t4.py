from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        mod = 10**9+7
        if int(low) > int(high):
            return 0
        @cache
        def f(i,mask,is_limit,is_num,s):
            if i ==len(s):
                return int(is_num)
            res =0
            if not is_num:
                res = f(i+1,mask,False,False,s) ##计算 0-9，10-99，100-999，1000-9999
            up = int(s[i]) if is_limit else 9
            for d in range(0 if is_num else 1, up +1):
                if is_num and abs(d-mask)==1:
                    res += f(i+1,d,is_limit and d == up,True,s)
                elif not is_num:
                    res += f(i+1,d,is_limit and d == up,True,s)
            return res
        f1 = f(0,0,True,False,high)
        f2 = f(0,0,True,False,str(int(low)-1))
        res = (f1-f2)%mod
        return res 




re =Solution().countSteppingNumbers(low = "1", high = "11")
print(re)
#Line 50: TypeError: 186278626472155847085563342621 is not valid value for the expected return type integer