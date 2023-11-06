from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf
from testInput import *

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.lazy = [0] * (4 * len(arr))
        self.build(1, 0, len(arr) - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update(self, node, start, end, left, right, value):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

        if start > right or end < left:
            return

        if start >= left and end <= right:
            self.tree[node] += (end - start + 1) * value
            if start != end:
                self.lazy[2 * node] += value
                self.lazy[2 * node + 1] += value
            return

        mid = (start + end) // 2
        self.update(2 * node, start, mid, left, right, value)
        self.update(2 * node + 1, mid + 1, end, left, right, value)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, left, right):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

        if start > right or end < left:
            return 0

        if start >= left and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_sum = self.query(2 * node, start, mid, left, right)
        right_sum = self.query(2 * node + 1, mid + 1, end, left, right)
        return max(left_sum,right_sum)

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        mx = 0
        mmx = max(nums)
        if mmx <0:
            return mmx
        ls = set([])
        for i,a in enumerate(nums):
            ls.add(a-i)
        ls = list(ls)
        ls.sort()
        dic ={}
        for i,a in enumerate(ls):
            dic[a] = i
        lss = [0]*len(ls)
        sg = SegmentTree(lss)
        n = len(lss)
        for i,a in enumerate(nums):
            t = dic[a-i]
            tm = sg.query(1,0,n,0,t)
            mx =max(mx,tm + a )
            tp = sg.query(1,0,n,0,t)
            if tp < tm+a:
                sg.update(1,0,n,t,t,tm+a-tp)
            #sg.updateRange(t,n-1,a)
            #print(i,a,mx,tm,0,t)
        return mx
        



re =Solution().maxBalancedSubsequenceSum(nums)
print(re)