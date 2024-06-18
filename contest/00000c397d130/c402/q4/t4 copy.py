from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf



class NumArray:
    __slots__ = 'nums', 'tree'

    def __init__(self, nums: List[int]):
        n = len(nums)
        tree = [0] * (n + 1)
        for i, x in enumerate(nums, 1):  # i 从 1 开始
            tree[i] += x
            nxt = i + (i & -i)  # 下一个关键区间的右端点
            if nxt <= n:
                tree[nxt] += tree[i]
        self.nums = nums
        self.tree = tree

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        i = index + 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def prefixSum(self, i: int) -> int:
        s = 0
        while i:
            s += self.tree[i]
            i &= i - 1  # i -= i & -i 的另一种写法
        return s

    def sumRange(self, left: int, right: int) -> int:
        if right < left:
            return 0
        return self.prefixSum(right + 1) - self.prefixSum(left)



class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        res = [0]*n
        for i in range(1,n-1):
            if nums[i]>nums[i-1] and nums[i]> nums[i+1]:
                res[i] =1
        sg = NumArray(res)
        
        def isGood(i):
            if i <0 or i >=n-1:
                return 0
            if nums[i]>nums[i-1] and nums[i]> nums[i+1]:
                return 1
            else:
                return 0
        
        ret =[]
        for t,f,t1 in queries:
            if t == 1:
                ret.append(sg.sumRange(f+1,t1-1))
            if t ==2:
                nums[f]=t1
                # for j in range(max(f - 1, 1), min(f + 2, n - 1)):
                #     sg.update(j,-isGood(j))
                nums[f]=t1
                for j in range(max(f - 1, 1), min(f + 2, n - 1)):
                    sg.update(j,isGood(j))
        return ret





re =Solution().countOfPeaks(nums = [7,10,7], queries = [[1,2,2],[2,0,6],[1,0,2]])
print(re)