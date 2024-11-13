# https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii/
# Range update  sum question 
from typing import List, Tuple, Optional
from collections import defaultdict,deque

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
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        dic= defaultdict(list)
        for i,(a,b) in enumerate(queries):
            dic[b].append((i,a))
        ls =[0]*2
        l = 0
        s = [int(a) for a in s]
        m = len(queries)
        ret = [-1]*m
        n = len(s)
        seg = SegmentTree([0]*n)
        #print(dic)
        for i,a in enumerate(s):
            ls[a] +=1
            while ls[0] > k and ls[1] > k:
                ls[s[l]] -=1
                l +=1
            #print(l,i,ls)
            seg.update(1,0,n,l,i,1)
            for idx,b in dic[i]:

                ret[idx] = seg.query(1,0,n,b,i)
               
        return ret

re =Solution().countKConstraintSubstrings(s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]])
print(re)