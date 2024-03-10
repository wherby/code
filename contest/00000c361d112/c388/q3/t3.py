from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        dic = defaultdict(set)
        for idx,wd in enumerate(arr):
            m = len(wd)
            for i in range(1,m+1):
                for j in range(m-i+1):
                    st = wd[j:j+i]
                    #$print(j,j+i-1,st,)
                    dic[st].add(idx)
        ret =[]
        #print(dic)
        for idx,wd in enumerate(arr):
            m = len(wd)
            isF = False
            for l in range(1,m+1):
                if isF== True: break
                fd =""
                for j in range(m-l+1):
                    st = wd[j:j+l]
                    #print(st)
                    if st not in dic or (st in dic and list(dic[st])==[idx]):
                        if fd =="":
                            fd= st
                        elif fd >st:
                            fd = st
                        isF =True
            if isF ==False:
                ret.append("")
            else:
                ret.append(fd)
        return ret





re =Solution().shortestSubstrings(["cab","ad","bad","c"])
print(re)