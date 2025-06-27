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
        stdic = {}
        for j in range(1,k+1):
            ls = []
            st  = allState(j,n)        
            for s1 in st:
                mx = 0
                acc = 0
                for i in range(n):
                    if (1<<i)& s1:
                        mx = max(mx,time[i])
                        acc += time[i]
                timedic[s1] = mx 
                ls.append((mx,s1))
            ls.sort()
            #print(ls)
            stdic[j] = [a[1] for a in ls]
        #print(stdic)
        visit={}


        @cache
        def dfs(state,Forward,m1):
            #print(state,Forward,m1)

            if (state,Forward, m1) not in visit:
                visit[(state,Forward,m1)] =1 
            else:
                return 10**10 
            if state ==0:
                return 0 
            ret = 10**10
            if Forward:
                for j in range(1,k+1):
                    st = stdic[j]
                    for s1 in st:
                        if s1 & state == s1:
                            t1 = timedic[s1]
                            ret = min(ret,t1* mul[m1] + dfs(state -s1,False,(m1+ int(t1* mul[m1])%m)%m))
            else:
                for j in range(1,2):
                    st = stdic[j]
                    for s1 in st:
                        if s1| state== state+ s1:
                            t1 = timedic[s1]
                            ret = min(ret,t1* mul[m1] + dfs(state +s1,True,(m1+ int(t1* mul[m1])%m)%m))
            #print(state)
            return ret


        ret=dfs((1<<n)-1,True,0)
        dfs.cache_clear()
        return ret
            





re =Solution().minTime( n = 3, k = 2, m = 4, time = [68,26,46], mul = [0.82,1.46,1.55,1.93])
#re =Solution().minTime( n = 2, k = 2, m = 4, time = [40,1], mul = [1.82,1.59,1.11,1.84])
re =Solution().minTime( n =4, k = 2, m = 5, time = [9,53,25,96], mul = [1.81,1.88,1.65,1.39,0.96])
re =Solution().minTime( n =3, k = 2, m = 3, time = [84,98,67], mul =[1.98,0.54,0.76])
re =Solution().minTime( n =3, k = 2, m = 2, time = [77,48,39], mul =[0.72,0.97])
print(re)

