from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        l,r = 0, 10**20
        
        
        def getLs(ls):
            n = len(ls)
            s1 =[]
            for i in range(n):
                for b in coins:
                    if ls[i]%b !=0:
                        c = ls[i]*b// math.gcd(ls[i],b)
                        s1.append(c)
            return list(s1)
        n = len(coins)
        res =[list(coins)]
        cur = list(coins)
        for i in range(n-1):
            cur = getLs(cur)
            res.append(cur)
        print(res)
        def verify(mid):
            sm = 0
            for i,ls in enumerate(res):
                for a in ls:
                    sm +=(-1)**i*mid//a
            return sm >=k
        while l<r:
            mid = (l+r)>>1
            if verify(mid):
                r = mid 
            else:
                l = mid+1
        return l





re =Solution().findKthSmallest([20,6,15,16,22],25727)
print(re)