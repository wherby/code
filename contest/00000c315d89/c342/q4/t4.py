from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from math import gcd

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        g = nums[0]
        for a in nums:
            g = gcd(a,g)
        if g !=1:
            return -1
        def verify(ls):
            g = ls[0]
            for a in ls:
                g =gcd(a,g)
            return g
        n=len(nums)
        acc =0
        for a in nums:
            if a !=1:
                acc +=1
        if acc !=n:
            return acc
        for l in range(2,50):
            for j in range(n-l+1):
                ls=nums[j:j+l]
                if verify(ls) ==1:
                    return l+n-2
        




re =Solution().minOperations([6,10,15])
print(re)