from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
from itertools import pairwise

from math import sqrt
class Solution:
    def primesUpTo(self, n):
        primes = set(range(2, n + 1))
        for i in range(2, n):
            if i in primes:
                it = i * 2
                while it <= n:
                    if it in primes:
                        primes.remove(it)
                    it += i
        return primes

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
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        pls =self.primesUpTo(2000)
        dic = defaultdict(int)
        for a in nums:
            r1 = self.getPrimeFactors(a,pls)
            for k,v in r1.items():
                #print(k,v)
                dic[k] += 1
        return len(dic.keys())





re =Solution().distinctPrimeFactors([2,4,3,7,10,6])
print(re)