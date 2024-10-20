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
    def numberOfSubstrings(self, s: str, k: int) -> int:
        
        n = len(s)
        cnt =0
        dic =defaultdict(int)
        lst = "-1"
        r = 0
        l=0
        while r<n:
            while dic[lst]<k and r<n:
                dic[s[r]] +=1
                lst = s[r]
                r +=1
            if dic[lst]>=k:
                while dic[lst] >=k:
                    cnt += n-r+1
                    dic[s[l]] -=1
                    l+=1
            #print(r,dic,cnt,l)
        return cnt



re =Solution().numberOfSubstrings( s = "abacb", k = 2)
print(re)