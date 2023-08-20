from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        if low>high:
            return 0

        @cache
        def f(i,mask,is_limit,is_num,s,b):
            n = len(s)
            if i ==len(s):
                #print(b,mask,is_num,mask%k==0)
                return int(is_num) and b ==0 and mask%k==0 
            res =0
            if not is_num:
                res = f(i+1,mask,False,False,s,b) ##计算 0-9，10-99，100-999，1000-9999
            up = int(s[i]) if is_limit else 9
            for d in range(0 if is_num else 1, up +1):
                aa = d*(10**(n-1-i)) %k
                #print(d,res,i)
                if   d %2==1:
                    res += f(i+1,mask+aa,is_limit and d == up,True,s,b+1)
                else :
                    res += f(i+1,mask+aa,is_limit and d == up,True,s,b-1)
            return res
        f1 = f(0,0,True,False,str(high),0)
        f2 = f(0,0,True,False,str(low-1),0)
        #print(f1)
        return f1-f2



re =Solution().numberOfBeautifulIntegers(low = 3, high = 31, k = 16)
print(re)