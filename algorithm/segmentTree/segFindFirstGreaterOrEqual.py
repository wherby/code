# https://leetcode.cn/contest/weekly-contest-440/problems/fruits-into-baskets-iii/description/
# simple version  of algorithm/segmentTree/segTreeWithFindFirst.py
from typing import List, Tuple, Optional
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(arr, 0, 0, self.n - 1)
    
    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        
        mid = (start + end) // 2
        self._build(arr, 2 * node + 1, start, mid)
        self._build(arr, 2 * node + 2, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def update(self, index, value):
        self._update(0, 0, self.n - 1, index, value)
    
    def _update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = value
            return
        
        mid = (start + end) // 2
        if index <= mid:
            self._update(2 * node + 1, start, mid, index, value)
        else:
            self._update(2 * node + 2, mid + 1, end, index, value)
        
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def find_first_greater_or_equal(self, query_val):
        result = self._find_first_greater_or_equal(0, 0, self.n - 1, query_val)
        return result if result != self.n else -1
    
    def _find_first_greater_or_equal(self, node, start, end, query_val):
        if self.tree[node] < query_val:
            return self.n
        
        if start == end:
            return start
        
        mid = (start + end) // 2
        left_result = self._find_first_greater_or_equal(2 * node + 1, start, mid, query_val)
        
        if left_result != self.n:
            return left_result
        
        return self._find_first_greater_or_equal(2 * node + 2, mid + 1, end, query_val)


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        st = SegmentTree(baskets)
        remain = 0
        for fruit in fruits:
            idx = st.find_first_greater_or_equal(fruit)
            if idx == -1:
                remain += 1
            else:
                st.update(idx, 0)
        return remain

re =Solution().numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4])
print(re)