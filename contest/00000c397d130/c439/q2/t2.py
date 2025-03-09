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
        for i in range(n):
            ls1= s[:i]
            ls2 = s[i+1:]
            t = min(len(ls1),len(ls2))
            k1 = k
            idx =1
            while idx<=t:
                if mind(ls1[-idx],ls2[idx-1]) <= k1:
                    k1 -=mind(ls1[-idx],ls2[idx-1])
                    mx = max(mx,1+idx*2)
                    #print(k1,idx,"a",i)
                    idx +=1
                else:
                    break
            ls1= s[:i]
            ls2 = s[i:]
            t = min(len(ls1),len(ls2))
            k1 = k
            idx =1
            while idx<=t:
                if mind(ls1[-idx],ls2[idx-1]) <= k1:
                    k1 -=mind(ls1[-idx],ls2[idx-1])
                    mx = max(mx,idx*2)
                    idx +=1
                else:
                    break
            print(mx,i)
        return mx



re =Solution().longestPalindromicSubsequence(s = "wehzr", k = 3)
print(re)
s1 = "wehzr"
for a in s1:
    print(ord(a))