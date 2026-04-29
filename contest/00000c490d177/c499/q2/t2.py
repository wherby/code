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
    def sortVowels(self, s: str) -> str:
        dic ={'a':0,'e':1,'i':2,'o':3 ,'u':4}
        ls =["a", "e", "i", "o", "u"]
        red = [[0,0,i] for i in range(5)]
        for i,a in enumerate(s):
            if a in dic:
                if red[dic[a]][0] == 0:
                    red[dic[a]][1] = -i 
                red[dic[a]][0] +=1
        red.sort()
        st =[]
        for m,_,i in red:
            st.extend([ls[i]]*m)
        ret= []
        print(red,st)
        for a in s:
            if a not in dic:
                ret.append(a)
            else:
                ret.append(st.pop())
        return "".join(ret)

            





re =Solution().sortVowels("aeiaaioooa")
print(re)