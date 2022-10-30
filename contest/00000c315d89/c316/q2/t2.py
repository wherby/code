from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

def gcd(a,b):
    while b:
        a,b = b,a %b
    return a
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n):
            gc =nums[i]
            for j in range(i,n):
                gc = gcd(gc,nums[j])
                if gc == k :
                    cnt +=1
                if gc %k != 0:
                    break
        return cnt



re =Solution().subarrayGCD(nums = [3,12,9,6], k = 3)
print(re)