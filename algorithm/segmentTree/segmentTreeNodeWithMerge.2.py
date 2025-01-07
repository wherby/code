# https://leetcode.cn/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/solutions/3039428/liang-chong-fang-fa-xian-duan-shu-qian-h-961z/
# 前后缀分解
from typing import List, Tuple, Optional


import math
INF  = math.inf

from math import ceil, log2
class Node:
  # ans:当前结果，s:区间总值， pre: 前缀， suf:后缀
  def __init__(self, ans=0,s =0,pre=0,suf=0):
    self.ans =ans
    self.s = s 
    self.pre =pre
    self.suf =suf
    
class SegmentTree:
  def __init__(self, arr):
    self.n = len(arr)
    self.tree = [None] *  ( 2**ceil(log2(len(arr))+1) - 1 ) # (4 * self.n)  # Double the size for segment tree
    self._build(arr, 0, self.n - 1, 0)

  def _build(self, arr, start, end, index):
    if start == end:
      ##TOD
      # Need to modify according to node definition
      self.tree[index] = Node(arr[start],arr[start], arr[start], arr[start])   
      return
    mid = (start + end) // 2
    self._build(arr, start, mid, 2 * index + 1)
    self._build(arr, mid + 1, end, 2 * index + 2)
    self.tree[index] = self._merge(self.tree[2 * index + 1], self.tree[2 * index + 2])

  ##TOD
  ## Using different node type need to change merge function
  def _merge(self, left, right):
    return Node(
        max(max(left.ans,right.ans), left.suf + right.pre),  # ans
        left.s + right .s,  # total
        max(left.pre,left.s+right.pre),  #pre
        max(right.suf,left.suf + right.s)  # suf
    )

  def update(self, index, value):

    self._update(index, value, 0, self.n - 1, 0)

  def _update(self, index, value, start, end, node_index):
    if start == end == index:                                     ## Tod
      self.tree[node_index] = Node(value, value, value, value)  # Need to modify according to node definition
      return
    mid = (start + end) // 2
    if index <= mid:
      self._update(index, value, start, mid, 2 * node_index + 1)
    else:
      self._update(index, value, mid + 1, end, 2 * node_index + 2)
    self.tree[node_index] = self._merge(self.tree[2 * node_index + 1], self.tree[2 * node_index + 2])

  def query(self, start, end):
    return self._query(start, end, 0, self.n - 1, 0).ans

  def _query(self, q_start, q_end, start, end, node_index):
    if q_start <= start and q_end >= end:
      return self.tree[node_index]
    if q_start > end or q_end < start:
      return Node()  # Empty node for out-of-range queries
    mid = (start + end) // 2
    left = self._query(q_start, q_end, start, mid, 2 * node_index + 1)
    right = self._query(q_start, q_end, mid + 1, end, 2 * node_index + 2)
    return self._merge(left, right)

from collections import defaultdict,deque
class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        seg  = SegmentTree(nums)
        dic = defaultdict(list)
        for i,a in enumerate(nums):
          if a <0:
            dic[a].append(i)
        ret = seg.tree[0].ans
        if ret <0:
          return ret
        #print(ret)
        for k,v in dic.items():
          for b in v:
            seg.update(b,0)
          ret = max(ret,seg.tree[0].ans)
          for b in v:
            seg.update(b,k)
          #print(k,v,ret,seg.tree[0].ans,)
        return ret
            
        





re =Solution().maxSubarraySum([-3,2,-2,-1,3,-2,3])
print(re)