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
        visit={}
        @cache
        def dfs(state,Forward,m1):
            #print(state,Forward,m1)
            if state ==0:
                return 0 
            ret = 10**10
            if Forward:
                for j in range(2,k+1):
                    st = allState(j,n)
                    for s1 in st:
                        if s1 & state == s1:
                            t1 = timedic[s1]
                            ret = min(ret,t1* mul[m1] + dfs(state -s1,False,(m1+ int(t1* mul[m1])%m)%m))

                st = allState(1,n)
                for s1 in st:
                    if s1 & state == s1:
                        if (state,m1,s1) not in visit:
                            visit[(state,m1,s1)] =1 
                        else:
                            continue
                        t1 = timedic[s1]
                        ret = min(ret,t1* mul[m1] + dfs(state -s1,False,(m1+ int(t1* mul[m1])%m)%m))
            else:
                for i in range(n):
                    if (1<<i)| state != state:
                        t1 = time[i]
                        ret = min(ret,t1* mul[m1] + dfs(state + (1<<i),True,(m1 + int(t1*mul[m1])%m)%m))
            #print(state)
            return ret


        ret=dfs((1<<n)-1,True,0)
        dfs.cache_clear()
        return ret

            





re =Solution().minTime( n = 3, k = 2, m = 4, time = [68,26,46], mul = [0.82,1.46,1.55,1.93])
re =Solution().minTime( n = 2, k = 2, m = 4, time = [40,1], mul = [1.82,1.59,1.11,1.84])
print(re)

