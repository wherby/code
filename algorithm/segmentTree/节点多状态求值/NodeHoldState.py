# https://leetcode.cn/contest/weekly-contest-399/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

from typing import List, Tuple, Optional


import math
INF  = math.inf

from math import ceil, log2
class Node:
  def __init__(self, ii=0, ie=0, ei=0, ee=0):
    self.ii = max(ii,ie,ei,ee)
    self.ie = max(ie,ee)
    self.ei = max(ei,ee) 
    self.ee = ee
    
    
class SegmentTree:
  def __init__(self, arr):
    self.n = len(arr)
    self.tree = [None] * ( 2**ceil(log2(len(arr))+1) - 1 ) # (4 * self.n)  # Double the size for segment tree
    self._build(arr, 0, self.n - 1, 0)

  def _build(self, arr, start, end, index):
    if start == end:
      ##TOD
      # Need to modify according to node definition
      self.tree[index] = Node(arr[start],0, 0, 0)   
      return
    mid = (start + end) // 2
    self._build(arr, start, mid, 2 * index + 1)
    self._build(arr, mid + 1, end, 2 * index + 2)
    self.tree[index] = self._merge(self.tree[2 * index + 1], self.tree[2 * index + 2])

  ##TOD
  ## Using different node type need to change merge function
  def _merge(self, left, right):
    return Node(
        max( left.ie + right.ii, left.ii + right.ei),  # incl
        max( left.ii + right.ee,left.ie+right.ie),  # excl
        max(left.ei+ right.ei,left.ee+ right.ii),  # left_excl_right_incl
        max(left.ei+ right.ee,left.ee + right.ie)  # left_incl_right_excl
    )

  def update(self, index, value):
    ##TOD
    # Need to modify according to node definition
    self._update(index, value, 0, self.n - 1, 0)

  def _update(self, index, value, start, end, node_index):
    if start == end == index:
      self.tree[node_index] = Node(value, 0, 0, 0)  # Need to modify according to node definition
      return
    mid = (start + end) // 2
    if index <= mid:
      self._update(index, value, start, mid, 2 * node_index + 1)
    else:
      self._update(index, value, mid + 1, end, 2 * node_index + 2)
    self.tree[node_index] = self._merge(self.tree[2 * node_index + 1], self.tree[2 * node_index + 2])

  def query(self, start, end):
    return self._query(start, end, 0, self.n - 1, 0).ii

  def _query(self, q_start, q_end, start, end, node_index):
    if q_start <= start and q_end >= end:
      return self.tree[node_index]
    if q_start > end or q_end < start:
      return Node()  # Empty node for out-of-range queries
    mid = (start + end) // 2
    left = self._query(q_start, q_end, start, mid, 2 * node_index + 1)
    right = self._query(q_start, q_end, mid + 1, end, 2 * node_index + 2)
    return self._merge(left, right)


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        mod = 10**9+7
        arr = []
        for a in nums:
            if a <0:
                a =0
            arr.append(a)
        sm = 0
        sg =SegmentTree(arr)
        for i,x in queries:
            if x <0:
                x =0
            sg.update(i,x)
            sm += sg.query(0,n-1)
            #print(sg.query(0,2),sg.query(0,1),sg.query(2,2))
            sm %=mod 
        return sm
        
        





re =Solution().maximumSumSubsequence([0,3,3,3,1,-2],[[4,0],[1,0]])
re= Solution().maximumSumSubsequence(nums = [3,5,9], queries = [[1,-2],[0,-3]])
re= Solution().maximumSumSubsequence([4,0,-1,-2,3,1,-1],[[3,1],[0,-2],[1,-1],[0,-2],[5,4],[6,-3],[6,-2],[2,-1]])
print(re)