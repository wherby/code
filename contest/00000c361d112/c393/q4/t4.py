from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n = len(nums)
        m = len(andValues)
        ret = 10**10
        dic=defaultdict(lambda:10**10)
        @cache
        def dfs(i,j,acc):
            nonlocal ret
            rev = 10**10
            if i ==n and j ==m :
                ret = min(ret,acc)
                return acc
            if j ==m or i==n or acc>=ret:
                return 10**10
            tmp = (2<<20)-1
            k = i
            cand = []
            while k<n and tmp >= andValues[j] :
                tmp = tmp &nums[k]
                k+=1
                if tmp == andValues[j] :
                    cand.append((k,j+1,acc +nums[k-1]))
            
            for nk,nj,nacc in cand[::-1]:
                if dic[(nk,nj)]> nacc:
                    ret= dfs(nk,nj,nacc)
                    rev = min(ret,rev)
                    if ret < 10**10:
                        dic[(nk,nj)] = nacc
            return rev
        dfs(0,0,0)
        return ret if ret != 10**10 else -1
            

re = Solution().minimumValueSum([1,3,2,4,7,5,3],[0,5,3])
print(re)


