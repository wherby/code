# https://leetcode.cn/problems/longest-balanced-subarray-ii/?envType=daily-question&envId=2026-02-11
# 这里实现单点更新 利用区间前缀和的 min max 信息快速查询前缀和等于某值的位置

from typing import List
import sys
import init_setting
from pythonLib.timefn import clock

class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        size = 4 * n
        self.sum = [0] * size
        self.minp = [0] * size  # min non-empty prefix sum
        self.maxp = [0] * size  # max non-empty prefix sum

    def _pull(self, idx: int):
        lc = idx * 2
        rc = idx * 2 + 1
        self.sum[idx] = self.sum[lc] + self.sum[rc]
        # non-empty prefixes: either in left, or all-left + non-empty in right
        self.minp[idx] = min(self.minp[lc], self.sum[lc] + self.minp[rc])
        self.maxp[idx] = max(self.maxp[lc], self.sum[lc] + self.maxp[rc])

    def update(self, pos: int, val: int, idx: int, l: int, r: int):
        if l == r:
            self.sum[idx] = val
            self.minp[idx] = val
            self.maxp[idx] = val
            return
        m = (l + r) // 2
        if pos <= m:
            self.update(pos, val, idx * 2, l, m)
        else:
            self.update(pos, val, idx * 2 + 1, m + 1, r)
        self._pull(idx)

    def find_first_prefix_eq(self, limit: int, target: int) -> int:
        """
        Return the smallest index i in [1..limit] such that prefixSum(i) == target,
        using the current w[].
        If not found, return -1.
        """
        if limit <= 0:
            return -1
        return self._find(1, 1, self.n, limit, 0, target)

    def _find(self, idx: int, l: int, r: int, limit: int, pre: int, target: int) -> int:
        if l > limit:
            return -1

        # Fully covered segment: we can prune using min/max reachable prefix sums.
        if r <= limit:
            if target < pre + self.minp[idx] or target > pre + self.maxp[idx]:
                return -1
            if l == r:
                return l
            m = (l + r) // 2
            left = idx * 2
            right = idx * 2 + 1
            ans = self._find(left, l, m, limit, pre, target)
            if ans != -1:
                return ans
            return self._find(right, m + 1, r, limit, pre + self.sum[left], target)

        # Partial coverage: recurse (left first). If limit <= mid, right is irrelevant.
        m = (l + r) // 2
        left = idx * 2
        right = idx * 2 + 1
        ans = self._find(left, l, m, limit, pre, target)
        if ans != -1:
            return ans
        if limit <= m:
            return -1
        # left is fully included when we go right in this case
        return self._find(right, m + 1, r, limit, pre + self.sum[left], target)


class Solution:
    @clock
    def longestBalanced(self, nums: List[int]) -> int:
        sys.setrecursionlimit(1_000_000)
        n = len(nums)
        seg = SegmentTree(n)
        last = [0] * (100000 + 1)  # nums[i] <= 1e5
        S = 0  # distinctEven - distinctOdd seen so far
        ans = 0

        for r in range(1, n + 1):
            x = nums[r - 1]
            sgn = 1 if (x & 1) == 0 else -1
            old = last[x]

            if old != 0:
                seg.update(old, 0, 1, 1, n)
            else:
                S += sgn  # first time seeing x changes distinct parity balance

            seg.update(r, sgn, 1, 1, n)
            last[x] = r

            if S == 0:
                ans = max(ans, r)  # x=0 => l=1
            else:
                i = seg.find_first_prefix_eq(r - 1, S)  # find smallest i in [1..r-1] with P(i)=S
                if i != -1:
                    ans = max(ans, r - i)

        return ans


from input import nums

re =Solution().longestBalanced(nums)
print(re)