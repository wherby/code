from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList


from math import sqrt



class Solution:
    def primesUpTo(self, n):
        visited=[0]*(n+2)
        res =[]
        for i in range(2,n+1):
            if visited[i]: continue
            res.append(i)
            for j in range(i,n+1,i):
                visited[j] =1
        return set(res)

    def getPrimeFactors(self, n, primes):
        ret = {}
        sq = int(sqrt(n))

        for p in primes:
            if n in primes:
                ret[n] = 1
                break

            while n % p == 0:
                ret[p] = ret.get(p, 0) + 1
                n //= p

            if n <= 1:
                break

        return ret
    def findValidSplit(self, nums: List[int]) -> int:
        dic1 =defaultdict(int)
        dic2 = defaultdict(int)
        primes = self.primesUpTo(10**6+3)
        for a in nums:
            pls = self.getPrimeFactors(a,primes)
            for k,v in pls.items():
                dic1[k] +=v 
        sm = len(dic1)
        for i,a in enumerate(nums[:-1]):
            pls = self.getPrimeFactors(a,primes)
            for k,v in pls.items():
                dic2[k] +=v 
                dic1[k] -=v 
                if dic1[k] ==0:
                    del dic1[k]
            if len(dic2) + len(dic1) == sm:
                return i 
        return -1
        





re =Solution().findValidSplit([4,7,8,15,3,5])
print(re)