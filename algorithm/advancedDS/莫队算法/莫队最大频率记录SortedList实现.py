
# https://leetcode.cn/contest/biweekly-contest-162/problems/threshold-majority-queries/submissions/649281456/
# 用 buk 记录区间频率的值，O(1)时间更新，其中mx记录最大频率
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


class Solution:
    def subarrayMajority(self, nums, queries):
        n = len(nums)
        block_size = int(n ** 0.5) + 1
        q = len(queries)
        
        # Store original indices
        queries_with_index = [(li, ri, threshold, i) for i, (li, ri, threshold) in enumerate(queries)]
        
        # Mo's order: even blocks ascending, odd blocks descending
        queries_with_index.sort(key=lambda x: (x[0] // block_size, x[1] if (x[0] // block_size) % 2 == 0 else -x[1]))
        
        freq = defaultdict(int)
        freq_of_freq = defaultdict(SortedList)  # 使用 SortedList 维护有序性
        max_freq = 0
        ans = [-1] * q
        
        current_li, current_ri = 0, -1
        
        def add(x):
            nonlocal max_freq
            if freq[x] > 0:
                freq_of_freq[freq[x]].discard(x)  # O(log n)
            freq[x] += 1
            freq_of_freq[freq[x]].add(x)         # O(log n)
            max_freq = max(max_freq, freq[x])
        
        def remove(x):
            nonlocal max_freq
            freq_of_freq[freq[x]].discard(x)     # O(log n)
            freq[x] -= 1
            if freq[x] > 0:
                freq_of_freq[freq[x]].add(x)     # O(log n)
            if not freq_of_freq[max_freq]:
                max_freq -= 1
        
        for li, ri, threshold, original_idx in queries_with_index:
            while current_li > li:
                current_li -= 1
                add(nums[current_li])
            while current_ri < ri:
                current_ri += 1
                add(nums[current_ri])
            while current_li < li:
                remove(nums[current_li])
                current_li += 1
            while current_ri > ri:
                remove(nums[current_ri])
                current_ri -= 1
            
            # 查询：找到第一个 >= threshold 且非空的 freq_of_freq[cnt]
            if max_freq < threshold:
                ans[original_idx] = -1
            else:
                cnt = max_freq
                while cnt >= threshold:
                    if freq_of_freq[cnt]:
                        ans[original_idx] = freq_of_freq[cnt][0]  # O(1) 获取最小值
                        break
                    cnt -= 1
                else:
                    ans[original_idx] = -1
        
        return ans

from input.input import nums,querys
re =Solution().subarrayMajority(nums,querys)
print(re)