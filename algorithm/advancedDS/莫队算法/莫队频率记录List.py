
# https://leetcode.cn/contest/biweekly-contest-162/problems/threshold-majority-queries/submissions/649281456/
# 用 elem_set 记录区间频率的值，也会有nlogn的损耗
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
from math import sqrt
INF  = math.inf

def compress(nums: List[int]):
    vals = sorted(set(nums))
    comp_map = {v: i for i, v in enumerate(vals)}
    return vals, comp_map

class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # 莫队
        n = len(nums)
        m = len(queries)
        if n == 0:
            return [-1] * m

        vals, comp_map = compress(nums)
        U = len(vals)
        comp_nums = [comp_map[x] for x in nums]

        block_sz = max(1, int(sqrt(n)))
        ans = [-1] * m
        query_idx = list(range(m))
        query_idx.sort(key=lambda i: (
            queries[i][0] // block_sz,
            queries[i][1] if (queries[i][0] // block_sz) % 2 == 0 else -queries[i][1]
        ))

        freq = [0] * U
        elem_set = SortedList()
        cur_l, cur_r = 0, -1

        def add(pos):
            c = comp_nums[pos]
            old_freq = freq[c]
            if old_freq > 0:
                elem_set.discard((old_freq, -c))
            new_freq = old_freq + 1
            elem_set.add((new_freq, -c))
            freq[c] = new_freq

        def remove(pos):
            c = comp_nums[pos]
            old_freq = freq[c]
            elem_set.discard((old_freq, -c))
            new_freq = old_freq - 1
            if new_freq > 0:
                elem_set.add((new_freq, -c))
            freq[c] = new_freq

        for idx in query_idx:
            l, r, threshold = queries[idx]
            while cur_l > l:
                cur_l -= 1
                add(cur_l)
            while cur_l < l:
                remove(cur_l)
                cur_l += 1
            while cur_r < r:
                cur_r += 1
                add(cur_r)
            while cur_r > r:
                remove(cur_r)
                cur_r -= 1

            if not elem_set:
                ans[idx] = -1
            else:
                max_freq, neg_c = elem_set[-1]
                c = -neg_c
                if max_freq >= threshold:
                    ans[idx] = vals[c]
                else:
                    ans[idx] = -1
        return ans

from input.input import nums,querys
re =Solution().subarrayMajority(nums,querys)
print(re)