from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n) - 1)
        l = len(n)
        half, v, ov = n[:l//2], int(n[:(l+1)//2]), int(n)
        res = set()
        s1, s2 = str(v-1), str(v + 1)
        res.add("9" * (l - 1))
        res.add("1" + "0" * (l - 1) + "1")
        if l % 2:
            res.add(s1[:-1] + s1[-1] + s1[:-1][::-1])
            res.add(s2[:-1] + s2[-1] + s2[:-1][::-1])
        else:
            res.add(s1 + s1[::-1])
            res.add(s2 + s2[::-1])
        if n[::-1] != n:
            res.add(half + n[l//2] + half[::-1] if l % 2 else half + half[::-1])
        # if n in res:
        #     res.remove(n)
        return res
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        target = -1
        if n%2 ==0:
            target = (nums[n//2] + nums[(n-1)//2])//2
        else:
            target= nums[n//2]
        ls = [int(a) for a in str(target)]
        
        if ls ==ls[::-1]:
            target = target
            return sum([abs(a-target) for a in nums])
        else:
            target = self.nearestPalindromic(str(target))
            sm = 10**20
            for a in target:
                sm = min(sm, sum([abs(int(a)- b ) for b in nums]))
            return sm
        
            



re =Solution().minimumCost([101,115,116,120,122])
print(re)