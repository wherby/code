from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution(object):
    def maximumStrength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        inf = 10**10
        dp =[[-inf,-inf] for i in range(k+1)]
        dp[0][0] = 0
        for a in nums:
            for i in range(k,0,-1):
                dp[i][1]= max( dp[i-1][0],dp[i][1])
                dp[i][1] =dp[i][1] +(-1)**(i+1)*(k+1-i)*a 
                dp[i][0]=max(dp[i][0],dp[i][1])
                #print(a,i,dp)
        #print(dp)
        return dp[k][0] 
        
        




re =Solution().maximumStrength([7,-70,75],1)
print(re)