# https://leetcode.cn/problems/find-the-k-sum-of-an-array/description/?envType=daily-question&envId=2024-03-09
# 生成 k 小的子序列

from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush 
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        sum = 0
        for i, x in enumerate(nums):
            if x >= 0:
                sum += x
            else:
                nums[i] = -x
        nums.sort()

        h = [(0, 0)]  # 空子序列
        for _ in range(k - 1):
            s, i = heappop(h)
            if i < len(nums):
                # 在子序列的末尾添加 nums[i]
                heappush(h, (s + nums[i], i + 1))  # 下一个添加/替换的元素下标为 i+1
                if i:  # 替换子序列的末尾元素为 nums[i]
                    heappush(h, (s + nums[i] - nums[i - 1], i + 1))
        return sum - h[0][0]