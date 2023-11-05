# https://leetcode.cn/contest/biweekly-contest-116/problems/subarrays-distinct-element-sum-of-squares-ii/
# 	from J_z10  https://leetcode.cn/contest/biweekly-contest-116/ranking/3/
from typing import List, Tuple, Optional

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
        return left_sum + right_sum
    
    
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        last_d = {}
        
        n = len(nums)
        t = SegmentTree([0] * n)
        
        t.update(1, 0, n, 0, 0, 1)
        last_d[nums[0]] = 0
        
        res = 1
        prev = 1
        mod = 10**9 + 7
        for i in range(1, len(nums)):
            v = nums[i]
            idx = last_d.get(v, -1)
            value = t.query(1, 0, n, idx+1, i-1)
            t.update(1, 0, n, idx+1, i, 1)
            length = i-idx
            prev = (prev + 2 * value + length) % mod
            #print(f'{i=} {idx=} {value=} {length=} {prev=}')
            res = (res + prev) % mod
            last_d[v] = i
            
        return res
test =[1,2,3,1]

import time

start = time.time()
re =Solution().sumCounts( test)
print(re)
end = time.time()
print(end - start)