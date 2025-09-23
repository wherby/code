
# https://leetcode.com/contest/weekly-contest-468/problems/maximum-total-subarray-value-ii/
from typing import List, Tuple, Optional
from sortedcontainers import SortedList

class SparseTable:
    def __init__(self, arr, op):
        n = len(arr)
        self.op = op
        self.lg = [0]*(n+1)
        for i in range(2, n+1):
            self.lg[i] = self.lg[i//2] + 1
        self.st = [arr[:]]
        j = 1
        while (1 << j) <= n:
            prev = self.st[j-1]
            step = 1 << (j - 1)
            cur = [None]*(n - (1 << j) + 1)
            for i in range(len(cur)):
                cur[i] = op(prev[i], prev[i+step])
            self.st.append(cur)
            j += 1

    def query(self, l, r):
        t = self.lg[r - l + 1]
        a = self.st[t][l]
        b = self.st[t][r - (1 << t) + 1]
        return self.op(a, b)

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sl = SortedList() # holds (diff, l, r)
        seen = set()
        
        stMin = SparseTable(nums, lambda a, b: a if a < b else b)
        stMax = SparseTable(nums, lambda a, b: a if a > b else b)
        seen.add((0,n-1))
        res = 0
        taken = 0
        def val(l, r):
            return stMax.query(l,r) - stMin.query(l,r)
        sl.add((val(0,n-1),0,n-1))
            
        while taken < k and sl:
            # print('op')
            v, l, r = sl.pop()
            res += v
            taken += 1
            if l + 1 <= r and (l+1,r) not in seen:
                seen.add((l+1,r))
                sl.add((val(l+1,r),l+1,r))
            if l <= r - 1 and (l,r-1) not in seen:
                seen.add((l,r-1))
                sl.add((val(l,r-1),l,r-1))
        return res