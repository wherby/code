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
    def longestBalanced(self, s: str) -> int:
        mx = 0
        def count(inch,outch):
            nonlocal mx
            #print(inch)
            n = len(inch)
            dic = {}
            start = [0]*n
            cur = [0]*n
            dic[tuple(cur)] = -1
            for i,a in enumerate(s):
                if a in inch:
                    t = inch.index(a)
                    cur[t] +=1
                    if all(c>0 for c in cur):
                        cur = [c-1 for c in cur]
                    ct = tuple(cur)
                    if ct in dic:
                        mx = max(mx,i-dic[ct])
                        #print(ct,i,dic[ct],dic)
                    else:
                        dic[ct] = i
                else:
                    dic = {}
                    cur= list(start)
                    dic[tuple(start)]=i 
        for stat in range(1,8):
            inch,outch =[],[]
            for j in range(3):
                if (1<<j)&stat:
                    inch.append(chr(ord('a') + j))
                else:
                    outch.append(chr(ord('a') + j))
            count(inch,outch)
            #print(inch,outch)
        return mx




re =Solution().longestBalanced("cbacccbaacc")
print(re)