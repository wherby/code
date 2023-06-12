from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        @cache
        def dfs(idx):
            #print(idx)
            if idx >= n:
                return 0 
            re = n-idx
            for d in dictionary:
                m = len(d)
                if s[idx:idx+m] == d :
                    re = min(re, dfs(idx+ m))
                    #print(re,d,dfs(idx+m),idx+m)
            re = min(re,dfs(idx+1)+1)
            #print(re,idx,n-idx)
            return re
        return dfs(0)
    
    





re =Solution().minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"])
print(re)