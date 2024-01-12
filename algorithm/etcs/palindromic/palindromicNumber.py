# https://leetcode.cn/contest/weekly-contest-376/problems/minimum-cost-to-make-array-equalindromic/

from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
import math

## 列举小于10**9 的所有回文数字
palindrome = []
for i in range(1, 10 ** 5 + 3):
    palindrome.append(int(str(i) + str(i)[::-1]))
    palindrome.append(int(str(i) + str(i)[:-1][::-1]))
palindrome.sort()

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        med = nums[n // 2]
        p = bisect_left(palindrome, med)
        ans = math.inf
        for i in range(p - 2, p + 3):
            ans = min(ans, sum(abs(x - palindrome[i]) for x in nums))
        return ans