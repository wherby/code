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

@cache
def allState(k,m):
    ret=[]
    state = (1<<k) -1
    while (state <(1<<m)):
        ret.append(state)
        c = state &(-state)
        r = state +c
        state= (((r ^ state) >>2)//c) |r 
    return ret

class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        if n ==1:
            return time[0]*mul[0]
        if k ==1:
            return -1


        timedic= {}
        for j in range(1,k+1):
            st  = allState(j,n)        
            for s1 in st:
                mx = 0
                for i in range(n):
                    if (1<<i)& s1:
                        mx = max(mx,time[i])
                timedic[s1] = mx 
        visit = defaultdict(lambda:10**10)

        stack =[(0,(1<<n)-1, True,0)]
        mn =10**10
        while stack:
            cst,state,Forward,m1 = heappop(stack)
            if state ==0:
                return cst
            #$print(stack)
            if cst > visit[(state,Forward,m1)]:
                continue
            visit[(state,Forward,m1)] =cst
            if Forward:
                for j in range(1,k+1):
                    st = allState(j,n)
                    for s1 in st:
                        if s1 & state == s1:
                            t1 = timedic[s1]
                            nm1 = (m1+ int(t1* mul[m1])%m)%m
                            if cst+ t1*mul[m1] < visit[(state -s1,False,nm1)]:
                                visit[(state -s1,False,nm1)] =cst+ t1*mul[m1]
                                heappush(stack,(cst+ t1*mul[m1],state -s1,False,nm1) )
            else:
                for j in range(1,k+1):
                    st = allState(j,n)
                    for s1 in st:
                        if s1| state== state+ s1:
                            t1 = timedic[s1]
                            nm1= (m1+ int(t1* mul[m1])%m)%m
                            if cst+ t1*mul[m1] < visit[(state +s1,True,nm1)]:
                                visit[(state +s1,True,nm1)] =cst+ t1*mul[m1]
                                heappush(stack,(cst+ t1*mul[m1],state +s1,True,nm1) )
        #print(visit)
        return mn





#re =Solution().minTime( n = 3, k = 2, m = 4, time = [68,26,46], mul = [0.82,1.46,1.55,1.93])
#re =Solution().minTime( n = 2, k = 2, m = 4, time = [40,1], mul = [1.82,1.59,1.11,1.84])
re =Solution().minTime( n = 11, k = 5, m = 3, time = [1,3,5,7,9,11,13,15,17,19,21], mul = [1.5,1.8,0.7])
print(re)

