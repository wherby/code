# https://leetcode.com/contest/biweekly-contest-90/problems/next-greater-element-iv/
# https://leetcode.com/problems/next-greater-element-iv/solutions/2756668/java-c-python-one-pass-stack-solution-o-n/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def secondGreaterElement(self, A: List[int]) -> List[int]:
        res, s1, s2 = [-1] * len(A), [], []
        for i,a in enumerate(A):
            while s2 and A[s2[-1]] < a:
                res[s2.pop()] = a
            tmp = []
            while s1 and A[s1[-1]] < a:
                tmp.append(s1.pop())
            s2 += tmp[::-1]
            s1.append(i)
        return res