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
        n = len(coins)
        coins.sort()
        s1 =set()
        for i in range(n):
            for j in range(i):
                c = coins[i]*coins[j]// math.gcd(coins[i],coins[j])
                s1.add(c)
        coins = [c for c in coins if c not in s1 ]
        n = len(coins)
        #print(coins)
        
        def getLs(coins):
            n = len(coins)
            s1 =set()
            for i in range(n):
                for j in range(i):
                    c = coins[i]*coins[j]// math.gcd(coins[i],coins[j])
                    s1.add(c)
        res =[]

        def verify(mid):
            sm = 0
            
            for a in coins:
                sm += mid //a 
            for c in s1:
                sm -= mid //c
            #print(s1,mid,sm)
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