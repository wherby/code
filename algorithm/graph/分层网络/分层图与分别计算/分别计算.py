# https://leetcode.cn/problems/minimum-time-to-reach-target-with-limited-power/description/


from heapq import heappop,heappush 
from typing import List, Tuple, Optional
class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        g = [[] for _ in range(n)]
        for a,b,c in edges:
            g[a].append((b,c))
        
        dpt = [10**10]* n 
        dpc = [1]* n 
        q  =[(0,-power,source)]
        resPower = -1 
        while q:
            ct,cp,a = heappop(q)
            if a == target :
                return [ct,-cp]
            if dpt[a] >ct or dpc[a] >cp:
                if dpt[a]>ct:
                    dpt[a] = ct 
                if dpc[a] > cp:
                    dpc[a] = cp 
                if cp +cost[a]<=0:
                    for b,c in g[a]:
                        heappush(q,(ct+c,cp+cost[a],b))

        return [-1,-1]