# https://leetcode.cn/problems/find-positive-integer-solution-for-a-given-equation/
from typing import List, Tuple, Optional

from bisect import bisect_right,insort_left,bisect_left
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for x in range(1, 1001):
            y = 1 + bisect_left(range(1, 1000), z, key=lambda y: customfunction.f(x, y))
            if customfunction.f(x, y) == z:
                ans.append([x, y])
        return ans
