# https://leetcode.cn/problems/minimum-cost-to-reach-destination-in-time/solutions/2937697/python3javacgotypescript-yi-ti-yi-jie-do-izg2/?envType=daily-question&envId=2024-10-03

from typing import List, Tuple, Optional
from collections import defaultdict,deque
from heapq import heapify,heappop,heappush 

from math import inf

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        g = [defaultdict(lambda :10**9) for _ in range(n)]
        for a,b,c in edges:
            g[a][b] = min(g[a][b],c)
            g[b][a] = min(g[b][a],c)
        
        cand = [(passingFees[0],0,0)]
        visit= defaultdict(lambda: 10**9)
        while cand:
            a,b,c = heappop(cand)
            if b > maxTime:
                continue
            if c == n-1:
                return a 
            if visit[c] <= b: # 如果是< 则超时  https://leetcode.cn/problems/minimum-cost-to-reach-destination-in-time/submissions/?envType=daily-question&envId=2024-10-03
                continue
            visit[c] = b 
            for d in g[c].keys():
                heappush(cand,(a + passingFees[d],b + g[c][d],d ))
        return -1
            

re =Solution().minCost(maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3])
print(re)
