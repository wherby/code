from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        ls=[0]*2002
        dic =defaultdict(list)
        dicc = {}
        for i,(s,e,c) in enumerate(tasks):
            dicc[i]=e-s +1-c
            for j in range(s,e+1):
                ls[j]+=1
                dic[j].append(i)
        sl = []
        for k,v in enumerate(ls):
            if v >0:
                sl.append((v,k))
        sl.sort()
        cnt = 0
        for _,k in sl:
            isG =True
            for a in dic[k]:
                if dicc[a]<=0:
                    isG =False
                    break
            if isG:
                for a in dic[k]:
                    dicc[a] -=1
                cnt +=1
        return len(sl) -cnt
        
        
        
            
        
        
        





re =Solution().findMinimumTime(tasks = [[1,10,7],[4,11,1],[3,19,7],[10,15,2]])
print(re)
