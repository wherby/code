from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
from collections import Counter
INF  = math.inf

class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        c = Counter(s)
        c0,c1 = c["0"],c["1"]
        ret = []
        n = len(s)
        for s1 in strs:
            c = Counter(s1)
            if c["0"]>c0 and c["1"]>c1:
                ret.append(False)
                continue
            s2 = [a for a in s1]
            cur =0
            while c["0"]<c0 and cur < n :
                if s2[cur] == "?":
                    s2[cur] = "0"
                    c["0"] +=1
                cur +=1
            for j in range(cur,n):
                if s2[j] =="?":
                    s2[j] = "1" 
            #print(s2) 
            acc = 0
            s2= "".join(s2)
            isGood = True
            #print(s,s2,c0,c1,c["0"],c["1"])
            for a,b in zip(s,s2):
                if a ==b:
                    continue
                if a =="1":
                    acc +=1
                else:
                    acc -=1
                if acc <0:
                    isGood = False
                    break
            if acc !=0:
                isGood = False 
            ret.append(isGood)
        return ret
                





re =Solution().transformStr(s = "101", strs = ["1?1","0?1","0?0"])
print(re)