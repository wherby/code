# https://leetcode.cn/problems/sort-array-by-increasing-frequency/
from collections import Counter
class Solution:
    def frequencySort(self, nums):
        cnt = Counter(nums)
        nums.sort(key=lambda x:[cnt[x], -x])
        return nums