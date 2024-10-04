# https://leetcode.cn/problems/minimum-cost-to-reach-destination-in-time/solutions/2937697/python3javacgotypescript-yi-ti-yi-jie-do-izg2/?envType=daily-question&envId=2024-10-03

from typing import List, Tuple, Optional
from math import inf
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        m,n = maxTime, len(passingFees)
        f =[[inf]*n for _ in range(m+1)]
        f[0][0] = passingFees[0]
        for i in range(1,m +1):
            for x,y,t in edges:
                if t <=i:
                    f[i][x] = min(f[i][x] , f[i-t][y] + passingFees[x] )
                    f[i][y] = min(f[i][y], f[i-t][x] + passingFees[y])
        ans = min(f[i][n-1] for i in range(m+1))
        return ans if ans <inf else -1
    
re =Solution().minCost(maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3])
print(re)
