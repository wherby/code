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
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        dic= defaultdict(list)
        for i in range(m):
            for j in range(n):
                dic[grid[i][j]].append((i,j))
        keys = list(dic.keys())
        keys.sort()
        keys=deque(keys)
        kst = [-1]
        mn = 10**30
        print(dic)
        @cache
        def dfs(i,j,k):
            nonlocal mn
            #print(i,j,k,grid[i][j],dic[grid[i][j]])
            if i== m-1 and j == n-1:
                return 0
            if i >=m or j >= n:
                return 10**30
            ret = 10**30
            if k >0 and   grid[i][j]>kst[-1]:
                print(i,j,"ccccccc")
                lk= kst[-1]
                while grid[i][j]>kst[-1]:
                    t1 = keys.popleft()
                    kst.append(t1)
                    tls = list(dic[t1])
                    
                    for a,b in tls:
                        ret = min(ret,dfs(a,b,k-1))
                    print(t1,tls,ret,i,j,"ccc",k)
                # while kst[-1] != lk:
                #     t1= kst.pop()
                #     keys.appendleft(t1)
            if i+1<m:
                ret = min(ret,dfs(i+1,j,k) + grid[i+1][j])
            if j + 1<n:
                ret =min(ret, dfs(i,j+1,k)+ grid[i][j+1])
            print(i,j,ret,"xx")
            return ret
        return dfs(0,0,k)



re =Solution().minCost(grid = [[25,13,10],[9,42,16]], k = 2)
print(re)