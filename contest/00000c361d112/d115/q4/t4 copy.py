from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
from collections import Counter



class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        c = Counter(nums)
        mod = 10**9+7
        keys =list( c.keys())
        n = len(keys)
        keys.reverse()
        @cache
        def dfs(i,acc):
            if acc>r:
                return 0
            if i == n:
                if l<=acc<=r:
                    return 1
                return 0
            ret =0
            for j in range(c[keys[i]] +1):
                ret += dfs(i+1,acc+j*keys[i])
            ret %= mod
            return ret
        return dfs(0,0)




re =Solution().countSubMultisets(nums = [1,2,1,3,5,2], l = 3, r = 5)
print(re)