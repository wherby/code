from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        ret = n+1 
        ls = [5**i for i in range(20)]
        #print(ls)
        def verify(ss):
            if ss[0] == "0":
                return False
            acc = 0 
            for a in ss:
                acc = acc*2+int(a)
            return acc in ls
        @cache
        def dfs(idx,st):
            nonlocal ret
            if idx ==n:
                ret = min(ret,st)
                return
            for j in range(idx+1,n+1):
                if verify(s[idx:j]):
                    dfs(j,st+1)
            return 
        dfs(0,0)
        return ret if ret!=n+1 else -1





re =Solution().minimumBeautifulSubstrings("1011")
print(re)