# https://leetcode.com/contest/weekly-contest-464/problems/maximum-walls-destroyed-by-robots/description/
from typing import List, Tuple, Optional



from bisect import bisect_right,insort_left,bisect_left
import math
INF  = math.inf

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        rd = [(r,d) for r,d in zip(robots,distance)]
        n = len(robots)
        rd.sort()
        walls.sort()
        lst0,lst1 = -10**6,-10**6
        dp0,dp1 = 0,0 
        def getCnt(l,r):
            if l >r:
                return 0
            ridx = bisect_right(walls,r)
            lidx = bisect_left(walls,l)
            return ridx -lidx

        for i,(r,d) in enumerate(rd):
            l0,r0 = r-d,r
            
            ndp0 = max(dp0 + getCnt(max(lst0,l0),r0), dp1+ getCnt(max(lst1,l0),r0))
            l1,r1 = r,r+d
            if i < n-1:
                r1 = min(r1, rd[i+1][0])
            ndp1 = max(dp0 + getCnt(l1,r1), dp1 + getCnt(max(lst1,l1),r1))
            dp0,dp1 = ndp0,ndp1
            lst0,lst1 = r0+1,r1+1
        return max(dp0,dp1)

            



robots = [31,36,18,39,10,21,40,69,57,51,19,32,50,53,3,28,9,59,46,22,13,63,33,14,25,52,64,5,44,17,68,45]
distance = [5,3,4,6,3,4,2,4,6,5,4,3,1,4,3,4,5,3,1,3,2,2,4,1,3,2,4,2,2,1,4,6]
walls = [10,41,54,6,7,33,14,30,9,12,38,27,39,52,42,46,45,17,2,15,55,44,4,18,20,34,28,51,11,13,37,31,23,24,5,56,22,57,35,29,32,26,48,47,16,43,36,25,53,19,40,49,21,1,50,3,8]

re =Solution().maxWalls(robots, distance , walls )
print(re)