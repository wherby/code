from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def adventureCamp(self, es: List[str]) -> int:
        es = [e.split("->") for e in es ]
        #print(es)
        ret = -1
        mx = 0
        dic = {}
        for a in es[0]:
            dic[a] =1
        #print(dic)
        dic[""] =1
        n = len(es)
        for i in range(1,n):
            acc =0
            for b in es[i]:
                if b not in dic:
                    acc+=1
                    dic[b] =1 
            if acc > mx:
                mx = acc 
                ret = i 
        return ret




re =Solution().adventureCamp( ["","Gryffindor->Slytherin->Gryffindor","Hogwarts->Hufflepuff->Ravenclaw"])
print(re)