from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        cnt =0
        g =defaultdict(list)
        ind =defaultdict(int)
        wei = defaultdict(int)
        for a,b in roads:
            g[a].append(b)
            g[b].append(a)
            ind[a]+=1
            ind[b] +=1
        
        visit={}
        cand =deque([])
        for k,v in ind.items():
            if v ==1 and k !=0:
                cand.append(k)
            wei[k] =1
        #print(cand)
        while cand:
            k = cand.popleft()
            visit[k] =1
            cnt += (wei[k]+seats-1) //seats 
            #print(cand,cnt,k,wei[k])
            for a in g[k]:
                if a in visit: continue
                wei[a] +=wei[k]
                ind[a] -=1
                if ind[a] ==1 and a !=0:
                    cand.append(a)
        return cnt                    
            




re =Solution().minimumFuelCost(roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2)
print(re)
re =Solution().minimumFuelCost(roads = [[0,1],[0,2],[0,3]], seats = 5)
print(re)
re =Solution().minimumFuelCost(roads = [], seats = 1)
print(re)
re =Solution().minimumFuelCost([[0,1],[1,2]],5)
print(re)