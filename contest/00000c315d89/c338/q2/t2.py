from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

def primeUpTo(n):
    primes = set(range(2,n+1))
    for i in range(2,n):
        if i in primes:
            it = i*2
            while it <=n:
                if it in primes:
                    primes.remove(it)
                it +=i 
    return primes
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        pls = list(primeUpTo(1000))
        pls.append(0)
        pls.append(10000)
        pls.sort()
        pres = 0
        for a in nums:
            a -= pres
            if a <= pls[0]:
                return False
            i = 0
            while i< len(pls) and a >pls[i+1]:
                i +=1
            pres += a - pls[i]
            #print(pres)
        return True
                
            




re =Solution().primeSubOperation( [2,2])
print(re)