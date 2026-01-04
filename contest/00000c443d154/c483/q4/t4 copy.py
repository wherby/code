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
    def minMergeCost(self, lists: List[List[int]]) -> int:

        n = len(lists)
        acc =0
        @cache
        def getMd(sa):
            nonlocal acc 
            print(sa)
            acc+=1
            la=[]
            for i in range(n):
                if (1<<i) &sa:
                    la.append(i)
            m = 0 
            for a in la:
                m +=len(lists[a])
            l = min(lists[a][0] for a in la)
            r = max(lists[a][-1] for a in la)
            while l <r:
                #print(l,r)
                md = (l+r)//2 
                cnt =0
                for a in la:
                    cnt += bisect_right(lists[a] ,md)
                if cnt >= (m+1)//2:
                    r = md 
                else:
                    l = md+1
            #print(m,l,cnt,la)
            return m,l

        @cache 
        def dfs(state):

            #print(state,lists)
            if len(state) ==1 :
                return 0 
            res = 10**20
            
            m = len(state)
            for i in range(m):
                for j in range(i):
                    nstate = list(state)
                    la,lb = state[i],state[j]
                    nstate.remove(la)
                    nstate.remove(lb)
                    lc = la +lb
                    nstate.append(lc)
                    nstate.sort()
                    m1,v1 = getMd(la)
                    m2,v2 = getMd(lb)
                    #print(m1,v1,m2,v2)
                    res = min(res,dfs(tuple(nstate))+ m1+m2+abs(v1-v2))
                    
            return res 
        n = len(lists)
        state = tuple([1<<i for i in range(n)])
        print(state)
        print(acc)
        return dfs(state)

                        

                    


from input import lists,lists2
print(len(lists))
print(len(lists2))
#lists = [[3,10],[1,3,8]]

re =Solution().minMergeCost(lists2 )
print(re)