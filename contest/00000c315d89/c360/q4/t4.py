from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        
        self.p[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1
            
class Solution:
    def getMaxFunctionValue(self, receiver: List[int], kk: int) -> int:
        n = len(receiver)
        ind = [0]*n
        #kk = kk+1
        for i,a in enumerate(receiver):
            ind[a] +=1
        dic = defaultdict(list)
        def dfs(i,acc,idx,k):
            visit2[i] =1
            acc += i 
            if len(dic[i]) ==2:
                return
            if len(dic[i])>0 and dic[i][0][2] != k:
                return
            dic[i].append((acc,idx,k))
            dfs(receiver[i],acc,idx+1,k)
        rings = {}
        rrings = defaultdict(list)
        visit2 ={}
        for i in range(n):
            if ind[i] ==0:
                dfs(i,0,1,i)
            #print(dic,i)
        for i in range(n):
            if i not in visit2:
                dfs(i,0,1,i)

        for i in range(n):
            if len(dic[i]) ==2:
                #print(dic[i])
                rings[i] = dic[i][1][2]
                rrings[dic[i][1][2]].append(i)
        #print(rings,rrings)
        #print(dic)
        visit = {}
        mx = 0
        acc = 0
        for idx in range(n):
            if ind[idx] ==0:
                acc=idx
                i = idx
                k=kk
                #print(idx,k,i,acc)
                while k>0:
                    k -=1
                    i = receiver[i]
                    acc +=i
                    #print(idx,k,i,acc,rings)
                    if i in rings and k> len(rrings[rings[i]]):
                        t = k // len(rrings[rings[i]])
                        k = k % len(rrings[rings[i]])
                        acc += (dic[i][1][0] -dic[i][0][0])*t
                #print(idx,acc)
                while idx not in visit:
                    mx  =max(mx,acc)
                    visit[idx] =1 
                    acc -=idx
                    idx = receiver[idx]
                    i = receiver[i]
                    acc += i
        for idx in range(n):
            if idx not in visit:
                acc=0
                acc += idx
                i = idx
                k=kk
                while k>0:
                    k -=1
                    i = receiver[i]
                    acc +=i
                    #print(idx,k,i,acc)
                    if i in rings and k> len(rrings[rings[i]]):
                        t = k // len(rrings[rings[i]])
                        k = k % len(rrings[rings[i]])
                        acc += (dic[i][1][0] -dic[i][0][0])*t
                while idx not in visit:
                    #print(idx,acc,i)
                    mx  =max(mx,acc)
                    visit[idx] =1 
                    acc -=idx
                    idx = receiver[idx]
                    i = receiver[i]

                    acc += i
        #print(visit)
        return mx



re =Solution().getMaxFunctionValue(receiver =[0,3,3,0],kk=10)
print(re)