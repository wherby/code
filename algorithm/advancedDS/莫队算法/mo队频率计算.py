# https://leetcode.cn/contest/weekly-contest-516/problems/valid-k-unique-subarrays-i/description/


from typing import List, Tuple, Optional
# common include
from collections import defaultdict,deque

class SubarrayChecker:
    def __init__(self, k: int):
        self.k = k
        self.freq = defaultdict(int)
        self.distinct_count = 0 
        self.even_count = 0    

    def add(self, x: int):
        f = self.freq[x]
        if f == 0:
            self.distinct_count += 1
        elif f % 2 == 0:
            self.even_count -= 1  
        
        self.freq[x] += 1
        if self.freq[x] % 2 == 0:
            self.even_count += 1  

    def remove(self, x: int):
        f = self.freq[x]
        if f % 2 == 0:
            self.even_count -= 1  

        self.freq[x] -= 1
        if self.freq[x] == 0:
            self.distinct_count -= 1
        elif self.freq[x] % 2 == 0:
            self.even_count += 1  

    def is_valid(self) -> bool:
        return self.distinct_count == self.k and self.even_count == self.k


def MoAlgo(nums: List[int], k: int, queries: List[List[int]]) -> List[bool]:
    n = len(nums)
    q = len(queries)
    if n == 0 or q == 0:
        return []

    block_size = max(1, int(math.sqrt(n)))

    query_index = [(li, ri, i) for i, (li, ri) in enumerate(queries)]

    def mo_cmp(q_item):
        li, ri, _ = q_item
        block = li // block_size
        return (block, ri) if block % 2 == 0 else (block, -ri)

    query_index.sort(key=mo_cmp)

    checker = SubarrayChecker(k)
    cur_li, cur_ri = 0, -1
    ans = [False] * q

    for li, ri, idx in query_index:
        while cur_li > li:
            cur_li -= 1
            checker.add(nums[cur_li])
        while cur_ri < ri:
            cur_ri += 1
            checker.add(nums[cur_ri])
        while cur_li < li:
            checker.remove(nums[cur_li])
            cur_li += 1
        while cur_ri > ri:
            checker.remove(nums[cur_ri])
            cur_ri -= 1

        ans[idx] = checker.is_valid()

    return ans

class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        return MoAlgo(nums,k,queries)