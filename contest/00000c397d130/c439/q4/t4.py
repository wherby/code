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
    def generateString(self, str1: str, str2: str) -> str:
        m,n = len(str1),len(str2)
        ret = ["" for _ in range(m+n-1) ]
        for i,a in enumerate(str1):
            if a == "T":
                for j in range(n):
                    if ret[i+j] =="" or ret[i+j] ==str2[j]:
                        ret[i+j] = str2[j]
                    else:
                        return ""
        #print(ret)
        cp = [a for a in str2]
        dic  = defaultdict(list)
        for i,a in enumerate(str1):
            if a == "F":
                for j in range(n):
                    dic[i+j].append(i)

        atoz = "abcdefghijklmnopqrstuvwxyz"
        for i,a in enumerate(ret):
            if a == "":
                for b in atoz:
                    ret[i] = b 
                    isG = True
                    for c in dic[i]:
                        if ret[c:c+n] ==cp:
                            isG = False
                    if isG == True:
                        break
                    ret[i] =""
                if ret[i] =="":
                    return ""
        #print(ret)
        for i,a in enumerate(str1):
            if a =="F":
                if ret[i:i+n] == cp:
                    return ""
        return "".join(ret)





#re =Solution().generateString(str1 = "TTFFT", str2 = "fff")
re =Solution().generateString(str1 = "FT", str2 = "aaa")
print(re)