from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def dfs(s1,acc,tar):
            if len(s1) ==0:
                return acc ==tar
            m = len(s1)
            for i in range(m):
                re= dfs(s1[i+1:],acc+ int(s1[:i+1]),tar)
                if re == True:
                    return True
            return False
        ret = 0
        for i in range(1,n+1):
            a = str(i*i)
            if dfs(a,0,i):
                #print(a,i,"x")
                ret +=i*i
            #print(ret,i)
        return ret





re =Solution().punishmentNumber(10)
print(re)