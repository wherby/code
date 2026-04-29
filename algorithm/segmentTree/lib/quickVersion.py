# https://leetcode.cn/contest/weekly-contest-499/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/submissions/721168041/
# 用模版 op函数会超时，直接实现不用函数调用更快 max 可以用fmax代替更快


class SegTree:
    def __init__(self, size: int):
        self.n = 1
        while self.n < size:
            self.n <<= 1
        self.tree = [0] * (2 * self.n)

    def update(self, idx: int, val: int):
        idx += self.n
        if self.tree[idx] >= val:
            return
        self.tree[idx] = val
        idx >>= 1
        while idx:
            new_val = max(self.tree[2 * idx], self.tree[2 * idx + 1])
            if self.tree[idx] == new_val:
                break
            self.tree[idx] = new_val
            idx >>= 1

    def query(self, l: int, r: int) -> int:
        if l > r:
            return 0
        l += self.n
        r += self.n
        res = 0
        while l <= r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if not (r & 1):
                res = max(res, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res


class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_val = max(nums)
        size = max_val + 2

        up_tree = SegTree(size)
        down_tree = SegTree(size)

        up = [0] * n
        down = [0] * n

        for i in range(n):
            j = i - k
            if j >= 0:
                up_tree.update(nums[j] - 1, up[j])
                down_tree.update(nums[j] - 1, down[j])
            v = nums[i]

            best_down = down_tree.query(0, v - 2) if v > 1 else 0
            best_up = up_tree.query(v, max_val - 1) if v < max_val else 0

            up[i] = v + best_down
            down[i] = v + best_up
        return max(max(up), max(down))