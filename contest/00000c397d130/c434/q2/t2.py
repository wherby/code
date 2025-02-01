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
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        ret= [0]*numberOfUsers
        rcd =[0]*numberOfUsers
        events.sort(key= lambda x:(int(x[1]), -ord(x[0][0])))
        #print(events)
        for a,b,c in events:
            b = int(b)
            if a =="MESSAGE":
                if c =="ALL":
                    for i in range(numberOfUsers):
                        ret[i] +=1
                elif c == "HERE":
                    for i in range(numberOfUsers):
                        if rcd[i] <= b:
                            ret[i] +=1
                else:
                    ls = c.split(" ")
                    for d in ls:
                        t = int(d[2:])
                        ret[t] +=1
            else:
                rcd[int(c)] = b+60
            #print(rcd,b,ret,c)
        return ret



#re =Solution().countMentions(3,[["MESSAGE","2","HERE"],["OFFLINE","2","1"],["OFFLINE","1","0"],["MESSAGE","61","HERE"]])
#print(re)
re =Solution().countMentions(3,[["MESSAGE","5","HERE"],["OFFLINE","10","0"],["MESSAGE","15","HERE"],["OFFLINE","18","2"],["MESSAGE","20","HERE"]])
print(re)