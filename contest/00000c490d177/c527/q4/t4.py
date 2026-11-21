# https://leetcode.cn/contest/weekly-contest-527/problems/count-valid-suffix-sorts-ii/description/
# mod = 10**9+7 会有碰撞，需要使用 2**61 - 1 这种梅森质数
from typing import List, Tuple, Optional

from collections import Counter


from collections import Counter
from typing import List


class SegmentTreeHash:
    def __init__(self, K: int, base: int, mod: int, pw: List[int]):
        """离散化值域线段树，用于维护降序排序后缀的动态哈希"""
        self.K = K
        self.BASE = base
        self.MOD = mod
        self.pw = pw  # 直接复用 StringHash 的幂次数组
        self.tree_cnt = [0] * (4 * K)
        self.tree_hash = [0] * (4 * K)

    def update(self, node: int, l: int, r: int, pos: int, val: int):
        if l == r:
            self.tree_cnt[node] += 1
            self.tree_hash[node] = (self.tree_hash[node] * self.BASE + val) % self.MOD
            return

        mid = (l + r) // 2
        if pos <= mid:
            self.update(2 * node, l, mid, pos, val)
        else:
            self.update(2 * node + 1, mid + 1, r, pos, val)

        left_node = 2 * node
        right_node = 2 * node + 1

        # 降序排列中：右子树（较大值）在前，左子树（较小值）在后
        self.tree_cnt[node] = self.tree_cnt[left_node] + self.tree_cnt[right_node]
        self.tree_hash[node] = (
            self.tree_hash[right_node] * self.pw[self.tree_cnt[left_node]]
            + self.tree_hash[left_node]
        ) % self.MOD

    @property
    def root_hash(self) -> int:
        return self.tree_hash[1]


class StringHash:
    def __init__(self, s1: List[int], base: int, mod: int):
        """区间哈希类（支持整数数组），内置幂次数组 pls"""
        n = len(s1)
        self.hls = [0] * (n + 1)
        self.pls = [1] * (n + 1)
        self.mod = mod
        self.base = base

        for i in range(n):
            self.hls[i + 1] = (self.hls[i] * self.base + s1[i]) % self.mod
            self.pls[i + 1] = (self.pls[i] * self.base) % self.mod

    def query(self, left: int, right: int) -> int:
        """获取子区间 [left, right) 的哈希值"""
        return (
            self.hls[right] - (self.hls[left] * self.pls[right - left]) % self.mod
        ) % self.mod


class Solution:
    def countSuffix(self, nums: List[int], target: List[int]) -> List[int]:
        n = len(nums)
        m = len(target)
        res_len = m - n + 1
        if res_len <= 0:
            return []

        BASE = 1000003
        MOD = 2**64
        all_vals = sorted(list(set(nums)))
        val_to_idx = {val: i for i, val in enumerate(all_vals)}
        K = len(all_vals)

        pref_hasher = StringHash(nums, BASE, MOD)
        pw = pref_hasher.pls
        st = SegmentTreeHash(K, BASE, MOD, pw)

        full_hash_counts = Counter()
        for i in range(n - 1, -1, -1):
            val = nums[i]
            pos = val_to_idx[val]
            st.update(1, 0, K - 1, pos, val)

            suffix_len = n - i
            prefix_hash_val = pref_hasher.query(0, i)
            sorted_suffix_hash = st.root_hash

            full_hash = (prefix_hash_val * pw[suffix_len] + sorted_suffix_hash) % MOD
            full_hash_counts[full_hash] += 1

        target_hasher = StringHash(target, BASE, MOD)
        ans = []
        for k in range(res_len):
            window_hash = target_hasher.query(k, k + n)
            ans.append(full_hash_counts[window_hash])

        return ans


re = Solution().countSuffix(nums=[2, 2, 3], target=[2, 2, 3, 2, 1, 3, 2, 2])
print(re)
