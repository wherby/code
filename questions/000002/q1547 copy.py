from typing import List, Tuple, Optional
from collections import defaultdict,deque
from functools import cache
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        ls =[0] + cuts +[n]
        n = len(ls)
        dp= defaultdict(lambda : 10**10)
        @cache
        def dfs(i,j):
            if j-i == 1:
                return 0 
            ret = 10**10 
            for k in range(i+1,j):
                ret = min(ret,dfs(i,k) + dfs(k,j) + ls[j] -ls[i])
            return ret
        return dfs(0,n-1)


re = Solution().minCost(n = 13, cuts = [3,12,1,5,9,11,4,8,7,2,6,10])
print(re)