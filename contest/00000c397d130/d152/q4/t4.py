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
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        g = [[] for _ in range(n)]
        for a,b,c  in edges:
            g[a].append((b,c))
            g[b].append((a,c))
        
        dic=defaultdict(int)
        ldic = defaultdict(int)
        visit= defaultdict(list)
        lastv= SortedList([])
        mx,mm = -1,-1
        lostdic = defaultdict(int)
        def dfs(a,p,acc,):
            nonlocal mx,mm
            visit[nums[a]].append(a)
            if len(visit[nums[a]]) > 1:
                l1 = ldic[visit[nums[a]][-2]]
                lastv.add((l1, visit[nums[a]][-2]))
            dic[a] = acc
            ldic[a] = ldic[p] +1
            t1,t2 = acc,ldic[a]
            if len(lastv) >=2:
                #print(lastv,lostdic)
                t1 =dic[a] -dic[lastv[-2][1]]-lostdic[lastv[-2][1]]
                t2 =ldic[a] - ldic[lastv[-2][1]]
            if t1 > mx:
                mx = t1
                mm = t2
            elif t1 ==mx and t2<mm:
                mm =t2
            for b,c in g[a]:
                if b == p: continue
                lostdic[a] =c
                dfs(b,a,acc+c)
            visit[nums[a]].pop()
            if len(visit[nums[a]])>0:
                l2 = ldic[visit[nums[a]][-1]]
                lastv.remove((l2,visit[nums[a]][-1]))
            #print(mm,mx,acc)
        dfs(0,-1,0)
        #print(dic,ldic)
        return [mx,mm]




re =Solution().longestSpecialPath(edges =[[5,0,4],[4,1,4],[4,3,4],[2,3,1],[2,7,6],[6,5,1],[7,5,1]], nums =[1,3,5,1,5,5,1,4])
print(re)