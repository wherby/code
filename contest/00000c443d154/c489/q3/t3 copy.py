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
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        def maxLen(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
 
            res = 0
            

            if l < 0 and r >= n:
                return n 
            

            if l >= 0:
                tl, tr = l - 1, r
                while tl >= 0 and tr < n and s[tl] == s[tr]:
                    tl -= 1
                    tr += 1

                res = max(res, tr - tl - 1)
            
            if r < n:
                tl, tr = l, r + 1
                while tl >= 0 and tr < n and s[tl] == s[tr]:
                    tl -= 1
                    tr += 1
                res = max(res, tr - tl - 1)
                
  
            res = max(res, r - l - 1)
            
            return res

        for i in range(n):
            max_len = max(max_len, maxLen(i, i))
            if i + 1 < n:
                max_len = max(max_len, maxLen(i, i + 1))
                
        return max_len



re =Solution().almostPalindromic("zzabba")  
print(re)