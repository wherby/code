from typing import List, Tuple, Optional
from collections import defaultdict,deque

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        ls =[0] + cuts +[n]
        n = len(ls)
        dp= defaultdict(lambda : 10**10)
        for i in range(n):
            dp[(i,i)] =0
        for i in range(n-1):
            dp[(i,i+1)] = 0
        for i in range(1,n): 
            for j in range(i-1,0,-1):
                for k in range(j+1,i):
                    #print(i,k,j, dp[(j,k)] + dp[(k+1,i)] + ls[i] -(ls[j-1] if j>0 else 0))
                    dp[(j,i)] = min(dp[(j,i)], dp[(j,k)] + dp[(k,i)] + ls[i] -(ls[j] ) )
                dp[(0,i)] = min(dp[(0,i)], dp[(0,j)] +dp[(j,i)] + ls[i] )
        return dp[(0,n-1)]

re = Solution().minCost(n = 13, cuts = [3,12,1,5,9,11,4,8,7,2,6,10])
print(re)