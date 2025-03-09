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
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        
        def mind(a,b):
            return min(abs(ord(a) -ord(b)) , 26 - abs(ord(a) -ord(b)))
        n = len(s)
        mx = 1

        @cache
        def dfs(i,j,k):
            if i == -1 or j == n:
                return 0 
            ret = 0
            if mind(s[i],s[j])<=k:
                ret = max(ret,dfs(i-1,j+1,k- mind(s[i],s[j]))+2)
            ret = max(ret,dfs(i-1,j,k))
            ret = max(ret,dfs(i,j+1,k))
            return ret
        for i in range(n):
            mx = max(mx,1+dfs(i-1,i+1,k))
            mx = max(mx,dfs(i,i+1,k))
        
        return mx



re =Solution().longestPalindromicSubsequence( s = "aaazzz", k = 4)
print(re)
